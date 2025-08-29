(help-download_zenodo_draft)=
# download_zenodo_draft.py - Download files from Zenodo draft deposits

## Description

This script downloads files from a Zenodo draft deposit using the Zenodo API. It can handle draft deposits that require authentication and provides advanced features like selective downloading and smart resuming.

## Usage

```bash
python3 tools/download_zenodo_draft.py RECORD_ID [--access-token TOKEN]
```

## Arguments

- **RECORD_ID** (Required) - Zenodo draft record ID
- **--access-token** (Optional) - Zenodo access token for authentication
- **--sandbox** (Optional) - Use Zenodo sandbox instead of production
- **--dry-run** (Optional) - Show what would be downloaded without downloading
- **--files** (Optional) - Download only specific files by number (comma-separated)

## Examples

```bash
# Download all files with access token
python3 tools/download_zenodo_draft.py 123456 --access-token your_token_here

# Show what would be downloaded (dry run)
python3 tools/download_zenodo_draft.py 123456 --sandbox --dry-run

# Download only specific files (use numbers from dry-run output)
python3 tools/download_zenodo_draft.py 123456 --files "1,3,5"
python3 tools/download_zenodo_draft.py 123456 --files "2"
```

## Authentication

### Environment Variables
```bash
export ZENODO_ACCESS_TOKEN=your_token_here
# or
export ZENODO_TOKEN=your_token_here
```

### .env File Support
Create a `.env` file with:
```
ZENODO_ACCESS_TOKEN=your_token_here
```
(requires python-dotenv: `pip install python-dotenv`)

### Token Priority Order
1. Command line `--access-token` argument
2. `ZENODO_ACCESS_TOKEN` or `ZENODO_TOKEN` environment variable
3. `.env` file with `ZENODO_ACCESS_TOKEN` or `ZENODO_TOKEN`

## Features

- **Smart resuming**: Won't re-download files that already exist with correct checksums
- **Selective download**: Choose specific files by number (use `--dry-run` first to see file numbers)
- **Multiple authentication methods**: Command line, environment variables, or .env file
- **Checksum verification**: Validates file integrity using Zenodo metadata
- **Metadata preservation**: Creates manifest and metadata files

## How It Works

1. **API Connection**: Connects to Zenodo API (production or sandbox)
2. **Metadata Fetch**: Retrieves metadata for the specified draft deposit
3. **File Validation**: Skips files that already exist with matching checksums
4. **Download**: Downloads selected files (or all files) to `zenodo-RECORD_ID` directory
5. **Checksum Storage**: Preserves checksums in `generated/manifest.zenodo-RECORD_ID.DATE.{sha256,md5}`
6. **Metadata Creation**: Creates file size metadata in `generated/metadata.zenodo-RECORD_ID.txt`

## Output Structure

```
zenodo-RECORD_ID/           # Downloaded files
generated/
├── manifest.zenodo-RECORD_ID.DATE.sha256
├── manifest.zenodo-RECORD_ID.DATE.md5
└── metadata.zenodo-RECORD_ID.txt
```

## Getting Access Tokens

You need a Zenodo access token to access draft deposits:

- **Production**: https://zenodo.org/account/settings/applications/tokens/new/
- **Sandbox**: https://sandbox.zenodo.org/account/settings/applications/tokens/new/

## Requirements

- Python 3.x
- requests: HTTP client library
- python-dotenv (optional): For .env file support

## Error Handling

- Validates access token and API connectivity
- Handles network failures gracefully
- Reports detailed error messages for API issues
- Validates checksums for downloaded files

This tool is essential for working with unpublished Zenodo deposits in research workflows that require access to draft materials.