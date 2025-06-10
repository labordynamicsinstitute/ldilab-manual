(help-sync-codeocean)=

# sync-codeocean.sh - Synchronize CodeOcean capsules with local repositories

## Description

This script manages synchronization between CodeOcean capsules and local Git repositories. It maintains both a live Git clone and a static copy of a CodeOcean capsule, keeping them synchronized with the remote capsule.

## Usage

```bash
./sync-codeocean.sh <codeocean-number>
```

## Parameters

- **codeocean-number** - The numeric ID of the CodeOcean capsule to sync

## Workflow

1. Creates or updates a live Git clone from CodeOcean (`codeocean-{number}-live`)
2. Creates or updates a static copy without Git metadata (`codeocean-{number}`)
3. Synchronizes changes from the live clone to the static copy
4. Stages changes in the current Git repository

## Output Directories

- `codeocean-{number}-live/` - Live Git clone of the CodeOcean capsule
- `codeocean-{number}/` - Static copy without Git metadata

## Dependencies

- Git (for cloning and repository operations)
- rsync (for file synchronization)
- Network access to git.codeocean.com

## Example

```bash
./sync-codeocean.sh 12345
```

Creates/updates:
- `codeocean-12345-live/` (Git clone)
- `codeocean-12345/` (static copy)

## Important Note

⚠️ **Warning**: The script removes all files in the static copy's code directory before syncing to ensure a clean update. Make sure any local changes are committed before running this script.

## How It Works

### Step 1: Live Clone Management
- If `codeocean-{number}-live` exists: Updates with `git pull`
- If it doesn't exist: Clones from `https://git.codeocean.com/capsule-{number}.git`

### Step 2: Static Copy Management
- If `codeocean-{number}` exists:
  - Runs `git pull` on current repository
  - Removes existing code files with `git rm`
  - Syncs from live clone using `rsync` (excluding `.git`)
  - Stages changes with `git add`
- If it doesn't exist:
  - Creates new directory
  - Syncs from live clone using `rsync` (excluding `.git`)

## Use Cases

This script is particularly useful for:
- **Research Replication**: Keeping local copies of CodeOcean computational environments
- **Version Control**: Maintaining both live connection and static snapshots
- **Collaboration**: Sharing CodeOcean content through standard Git workflows
- **Archive Management**: Creating clean copies without CodeOcean-specific Git metadata

## File Synchronization

The script uses `rsync -auv --exclude ".git"` which:
- `-a`: Archive mode (preserves permissions, timestamps, etc.)
- `-u`: Update only (skip files that are newer on receiver)
- `-v`: Verbose output
- `--exclude ".git"`: Excludes Git metadata from static copy

This ensures the static copy contains only the content files without Git history.
