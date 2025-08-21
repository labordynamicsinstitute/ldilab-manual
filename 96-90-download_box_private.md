(help-download_box_private)=

# download_box_private.py - Download files from private Box folders

## Description

This script downloads files from a private Box folder using JWT authentication. It's designed for secure access to private research data stored in Box with proper authentication credentials.

## Usage

```bash
download_box_private.py SUBFOLDER [options]
```

## Arguments

- **SUBFOLDER** (Required) - Subfolder identifier (downloads from 'aearep-SUBFOLDER')

## Example

```bash
download_box_private.py 1234  # Download from subfolder 'aearep-1234'
```

## Environment Variables

Required for authentication:

- **BOX_FOLDER_PRIVATE** - Box folder ID to download from
- **BOX_PRIVATE_KEY_ID** - Box JWT public key ID
- **BOX_ENTERPRISE_ID** - Box enterprise ID
- **BOX_CLIENT_ID** - Box client ID (optional if using config file)
- **BOX_CLIENT_SECRET** - Box client secret (optional if using config file)

Optional configuration:

- **BOX_CONFIG_PATH** - Directory containing the Box config file
- **BOX_OUTPUT_DIR** - Directory to download files to (default: ./restricted)
- **BOX_PRIVATE_JSON** - Base64 encoded content of the Box config JSON file

## Base64 Configuration

For CI/CD environments, you can provide the entire Box configuration as a base64-encoded string:

```bash
# Generate base64 config
cat config.json | base64

# Set environment variable
export BOX_PRIVATE_JSON="base64_encoded_string_here"
```

## Authentication Methods

### 1. Environment Variables
Set individual Box API credentials as environment variables.

### 2. Config File
Place Box JWT configuration file in the directory specified by `BOX_CONFIG_PATH`.

### 3. Base64 Encoded Config
Provide entire configuration as base64-encoded string in `BOX_PRIVATE_JSON`.

## Features

- **JWT Authentication**: Secure access using Box JWT authentication
- **Flexible Configuration**: Multiple authentication methods for different environments
- **Organized Downloads**: Downloads to organized folder structure
- **Error Handling**: Comprehensive error handling for API failures
- **Logging**: Configurable logging for debugging and monitoring

## Output Structure

```
restricted/                 # Default output directory (configurable)
└── aearep-SUBFOLDER/      # Downloaded files from specified subfolder
    ├── file1.txt
    ├── file2.pdf
    └── ...
```

## Requirements

- Python 3.x
- boxsdk: Box Python SDK
- Valid Box JWT application credentials

## Box Application Setup

To use this script, you need:

1. **Box Developer Account**: Create at https://developer.box.com/
2. **JWT Application**: Create a new JWT application in Box Developer Console
3. **Authentication Keys**: Download the JWT configuration file
4. **Folder Access**: Ensure the application has access to the target folder

## Security Considerations

- Store JWT credentials securely
- Use environment variables in production
- Limit application permissions to necessary scopes
- Regularly rotate authentication credentials

## Error Handling

- Validates authentication credentials before proceeding
- Handles network failures and API rate limits
- Reports detailed error messages for troubleshooting
- Graceful handling of missing files or permissions

This tool is essential for research workflows that require secure access to private datasets stored in Box repositories.