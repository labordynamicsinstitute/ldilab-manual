(help-download_openicpsr-private)=
# download_openicpsr-private.py - Download files from private openICPSR deposits

## Description

This script authenticates with openICPSR and downloads all files from a private deposit as a ZIP archive, then extracts it to a local directory. It's designed for downloading draft/unpublished deposits that require authentication and are not publicly accessible.

## Usage

```bash
python3 tools/download_openicpsr-private.py PROJECT_ID [path] [login]
```

## Arguments

- **PROJECT_ID** (Required) - Numeric openICPSR project ID (must be digits only)
- **path** (Optional) - Download directory (default: current directory)
- **login** (Optional) - Email for interactive authentication (will prompt for password)

## Examples

```bash
# Using environment variables for authentication
export ICPSR_EMAIL="your.email@domain.com"
export ICPSR_PASS="your_password"
python3 tools/download_openicpsr-private.py 123456

# Specifying download path
python3 tools/download_openicpsr-private.py 123456 ./downloads

# Interactive login (will prompt for password)
python3 tools/download_openicpsr-private.py 123456 ./downloads your.email@domain.com

# Using config file (config.yml with openicpsr: PROJECT_ID)
python3 tools/download_openicpsr-private.py
```

## Authentication Methods

The script supports multiple authentication methods in order of preference:

1. **Interactive Authentication**: Command line login + password prompt
2. **Environment Variables**: `ICPSR_EMAIL` and `ICPSR_PASS`
3. **Config File**: `config.yml` with `openicpsr: PROJECT_ID`

## Environment Variables

- **ICPSR_EMAIL** - Your openICPSR account email
- **ICPSR_PASS** - Your openICPSR account password
- **DEBUG** - Enable debug output (any non-empty value)

## Features

- **Multiple Authentication Methods**: Flexible authentication for different environments
- **Automatic Extraction**: Downloads ZIP and extracts to organized directory
- **Config File Support**: Integration with YAML configuration files
- **Debug Mode**: Detailed logging for troubleshooting
- **Secure Password Handling**: Interactive password prompts for security

## How It Works

1. **Authentication**: Authenticates with openICPSR using provided credentials
2. **Project Access**: Accesses private/unpublished deposit by PROJECT_ID
3. **Download**: Downloads complete deposit as ZIP archive
4. **Extraction**: Extracts ZIP contents to local directory
5. **Organization**: Maintains file structure from original deposit

## Output Structure

```
PROJECT_ID/                 # Directory named after project ID
├── data/                   # Extracted data files
├── programs/               # Code and scripts
├── documentation/          # README and documentation
└── ...                     # Other deposit contents
```

## Config File Format

Create a `config.yml` file with:
```yaml
openicpsr: 123456  # Your project ID
```

## Security Considerations

- **Credentials**: Store credentials securely using environment variables
- **Interactive Mode**: Use interactive password prompts in shared environments
- **Debug Mode**: Avoid debug mode in production to prevent credential logging
- **Access Control**: Ensure only authorized users have access to private deposits

## Error Handling

- Validates PROJECT_ID format (digits only)
- Handles authentication failures gracefully
- Reports download and extraction errors
- Provides detailed error messages for troubleshooting

## Requirements

- Python 3.x
- requests: HTTP client library
- PyYAML: YAML configuration file support
- Valid openICPSR account with access to target deposit

This tool is essential for research workflows that require access to unpublished or private openICPSR deposits during the replication process.