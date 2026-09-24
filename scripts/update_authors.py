#!/usr/bin/env python3
"""Regenerate the author list from the repository's GitHub contributors.

Updates two places:
  - the `author:` line in _config.yml (plain names; used in the footer and PDF)
  - the block between the authors markers in index.md (names linked to GitHub)

Names are resolved in this order: scripts/authors.csv, then the GitHub profile
name (if it looks like a first and last name), then the GitHub login.
Rows in authors.csv without a `github` value are authors who never committed
here (e.g., contributors to the earlier manual); they are always included.
Rows with `exclude` set are dropped. Lars Vilhuber is always listed first.

Usage: scripts/update_authors.py [--add LOGIN ...]
Set GITHUB_TOKEN (or GH_TOKEN) to avoid API rate limits.
"""

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "labordynamicsinstitute/ldilab-manual")
FIRST = "larsvilhuber"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOOKUP = os.path.join(ROOT, "scripts", "authors.csv")
CONFIG = os.path.join(ROOT, "_config.yml")
INDEX = os.path.join(ROOT, "index.md")
START, END = "<!-- authors:start -->", "<!-- authors:end -->"


def api(path):
    req = urllib.request.Request(f"https://api.github.com/{path}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def contributors():
    logins, page = [], 1
    while True:
        batch = api(f"repos/{REPO}/contributors?per_page=100&page={page}")
        if not batch:
            return logins
        logins += [c["login"] for c in batch if c.get("type") == "User"]
        page += 1


def looks_human(name, login):
    return bool(name) and name.lower() != login.lower() and len(name.split()) >= 2


def sort_key(name):
    folded = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    parts = folded.lower().split()
    return (parts[-1], parts[:-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--add", nargs="*", default=[],
                        help="extra GitHub logins (e.g., a just-merged PR author)")
    args = parser.parse_args()

    with open(LOOKUP, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    known = {r["github"].lower(): r for r in rows if r["github"]}

    authors = {}  # login (lowercased) or name -> (name, login)
    for login in dict.fromkeys(contributors() + args.add):
        row = known.get(login.lower())
        if row and row["exclude"].strip():
            continue
        if row and row["name"]:
            name = row["name"]
        else:
            profile = (api(f"users/{login}").get("name") or "").strip()
            if looks_human(profile, login):
                name = profile
            else:
                name = login
                print(f"warning: no human name for '{login}'; add it to {LOOKUP}",
                      file=sys.stderr)
        authors[login.lower()] = (name, login)
    for r in rows:
        if not r["github"] and r["name"] and not r["exclude"].strip():
            authors.setdefault(r["name"], (r["name"], None))

    first = authors.pop(FIRST, None) or (known[FIRST]["name"], FIRST)
    ordered = [first] + sorted(authors.values(), key=lambda a: sort_key(a[0]))

    plain = ", ".join(name for name, _ in ordered)
    with open(CONFIG, encoding="utf-8") as f:
        config = f.read()
    config = re.sub(r"(?m)^author:.*$", lambda _: f"author: {plain}", config, count=1)
    with open(CONFIG, "w", encoding="utf-8") as f:
        f.write(config)

    linked = ", ".join(f"[{name}](https://github.com/{login})" if login else name
                       for name, login in ordered)
    with open(INDEX, encoding="utf-8") as f:
        index = f.read()
    if START not in index or END not in index:
        sys.exit(f"error: {INDEX} is missing the {START} / {END} markers")
    index = re.sub(re.escape(START) + r".*?" + re.escape(END),
                   lambda _: f"{START}\n{linked}\n{END}", index, flags=re.S)
    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(index)

    print(plain)


if __name__ == "__main__":
    main()
