# Deployment & PR previews

This repo's manual is built with Jupyter Book and published to `gh-pages`
via [.github/workflows/main.yml](.github/workflows/main.yml). That workflow
has four jobs:

- **build** — always runs (push to `main`, pull requests). Builds the
  Jupyter Book HTML and uploads it as a workflow artifact named
  `book-html`.
- **build-pdf** — always runs alongside `build`. Builds the printable PDF
  and uploads it as a workflow artifact named `book-pdf`.
- **deploy** — runs only on pushes to `main`. Downloads `book-html` (and
  `book-pdf`, if it built successfully) and pushes them to the `gh-pages`
  branch, which serves the live site.
- **preview** — runs on pull requests opened from a branch of this
  repository (not a fork). Downloads the `book-html` artifact and deploys
  it to [Cloudflare Pages](https://pages.cloudflare.com/) as a per-PR
  preview, then posts (or updates) a comment on the PR with the preview
  link.

Forked PRs never run the `preview` job's deploy step, since forks don't have
access to repository secrets — that's a GitHub Actions security boundary,
not a bug.

The Cloudflare Pages **project name is derived automatically** from the
GitHub repository name (`${{ github.event.repository.name }}` in the
workflow) — currently `ldilab-manual`. Nothing in the workflow needs
editing if the repo is ever renamed; only the one-time Cloudflare project
creation below needs to match.

## One-time Cloudflare Pages setup

You need a Cloudflare account and an API token before the `preview` job can
deploy anything.

1. **Create the Cloudflare API token.**
   In the Cloudflare dashboard: **My Profile → API Tokens → Create Token**,
   using a custom token with `Account.Cloudflare Pages: Edit` permission.
   Copy the token value — it's only shown once.

2. **Find your Cloudflare Account ID.**
   It's shown on the right-hand sidebar of any zone/domain overview page in
   the Cloudflare dashboard, or via `wrangler whoami` if you have Wrangler
   installed locally.

3. **Set both as GitHub Actions secrets on this repo**, using the `gh` CLI
   (run from the repo root, or add `--repo labordynamicsinstitute/ldilab-manual`
   from elsewhere):

   ```bash
   gh secret set CLOUDFLARE_API_TOKEN --body "<paste the API token>"
   gh secret set CLOUDFLARE_ACCOUNT_ID --body "<paste the account ID>"
   ```

   Or omit `--body` to be prompted / pipe the value in:

   ```bash
   gh secret set CLOUDFLARE_API_TOKEN
   echo -n "<account id>" | gh secret set CLOUDFLARE_ACCOUNT_ID
   ```

   If you keep these values in 1Password, pipe them straight from the `op`
   CLI instead of copy-pasting. This assumes a `cloudflare.com` item with
   an "Account ID" field and a per-repo "API token: `<repo>`" field:

   ```bash
   REPO="$(basename "$(git rev-parse --show-toplevel)")"
   op item get "cloudflare.com" --fields "API token: $REPO" | gh secret set CLOUDFLARE_API_TOKEN
   op item get "cloudflare.com" --fields "Account ID" | gh secret set CLOUDFLARE_ACCOUNT_ID
   ```

4. **Create the Cloudflare Pages project.** This must be done locally,
   before opening a preview PR — `wrangler pages deploy` in CI does not
   create the project on its own. Create it once with
   [Wrangler](https://developers.cloudflare.com/workers/wrangler/)
   (requires Node.js), run from the repo root so the project name is
   picked up from the checkout directory rather than typed by hand, and
   set `main` as the production branch:

   ```bash
   npx wrangler login
   npx wrangler pages project create "$(basename "$(git rev-parse --show-toplevel)")" --production-branch main
   ```

5. **Verify the secrets are set:**

   ```bash
   gh secret list
   ```

   You should see `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` listed
   (values are never shown, only names and update times).

## After setup

Once the secrets exist, every PR from a repo branch (not a fork) will get:

- A live preview at a Cloudflare Pages URL specific to that PR
  (`--branch=pr-<PR number>`), rebuilt on every push to the PR.
- A PR comment with the preview link, edited in place on each new commit
  rather than re-posted.

## If the repository is ever renamed

The Cloudflare Pages project name must be created to match the new
repository name (Cloudflare project names can't easily be renamed once
created). If you rename this repo, create a new Cloudflare Pages project
matching the new name (step 4 above) — the workflow itself needs no
changes, since it reads the project name from GitHub at deploy time.
