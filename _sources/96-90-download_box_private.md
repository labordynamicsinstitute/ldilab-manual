(help-download_box_private)=

# download_box_private.py - Download files from private Box folders

## Description

This script downloads files from a private Box folder using JWT authentication. It's designed for secure access to private research data stored in Box with proper authentication credentials.

## Usage

```bash
python tools/download_box_private.py [SUBFOLDER] 
```

### Arguments

- **SUBFOLDER** (optional) - Subfolder identifier (downloads from 'aearep-SUBFOLDER'). This will be the tag of the main Jira ticket, such as aearep-1234. If empty, will be deduced from the current directory name.

### Example

```bash
python tools/download_box_private.py 1234  # Download from subfolder 'aearep-1234'
```

or

```bash
cd /path/to/aearep-1234
python tools/download_box_private.py   # Download from subfolder 'aearep-1234'
```

## Requirements

- Python >= 3.9
- `boxsdk`: Box Python SDK
- Valid Box JWT application credentials

### Installing Box SDK

- This can be done through conda, or in pip, or pipx. 
- The above dependencies can be installed by executing 

```
pip install -r requirements.txt
```

in any recent repository updated with "tools" newer than June 7, 2025.

Ideally, these should be installed in your main Python environment, since you will be re-using this regularly. You can also install in a virtual environment. 

If using `conda`, you can install `boxsdk` with:

```shell
conda install boxsdk
conda install boxsdk[jwt]
```

- Currently, box is updating boxsdk to box-sdk-gen. This script will work only with `boxsdk`, not the newer `box-sdk-gen`. 


## Using AEA Credentials

To permantently set the proper credentials on BioHPC, you can modify your `~/.bashrc` profile, to include the box environmental variables. These values can be obtained from a supervisor.

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
└──                         # Downloaded files from specified subfolder
    ├── file1.txt
    ├── file2.pdf
    └── ...
```

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

