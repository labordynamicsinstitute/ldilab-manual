(help-download_dv)=

# download_dv.py - Download datasets from Dataverse repositories

## Description

This script downloads complete datasets from Dataverse instances (like Harvard Dataverse) using their DOI (Digital Object Identifier) and the Dataverse API. It creates organized directory structures and automatically extracts downloaded ZIP files.

## Usage

```bash
python3 tools/download_dv.py --doi DOI [--server_url URL] [--output PATH]
```

## Arguments

- **--doi** (Required) - DOI of the dataset (e.g., "doi:10.7910/DVN/ABC123")
- **--server_url** (Optional) - Dataverse server URL (default: https://dataverse.harvard.edu)
- **--output** (Optional) - Output directory (default: current directory)

## Examples

```bash
# Download from Harvard Dataverse (default)
python3 tools/download_dv.py --doi "doi:10.7910/DVN/ABC123"

# Download from custom Dataverse instance
python3 tools/download_dv.py --doi "doi:10.7910/DVN/ABC123" --server_url "https://dataverse.example.edu"

# Specify custom output directory
python3 tools/download_dv.py --doi "doi:10.7910/DVN/ABC123" --output "./downloads"
```

## Features

- Downloads entire dataset as ZIP archive using Dataverse API
- Creates organized directory structure: `dv-[PUBLISHER]-[DATASET_ID]`
- Automatic extraction of downloaded ZIP files
- Progress feedback during download
- Automatic git integration in CI environments
- Skips re-extraction if target directory already exists

## API Usage

- Uses Dataverse Native API to get dataset metadata
- Downloads files in original format via dataset access API
- Supports public datasets (no authentication required)

## Output Structure

```
Input DOI: doi:10.7910/DVN/ABC123
Output directory: ./dv-DVN-ABC123/
Downloaded file: ./dv-DVN-ABC123/ABC123.zip (extracted automatically)
```

## Error Handling

- Validates DOI format and dataset availability
- Handles download failures gracefully
- Reports API errors and connection issues

## Requirements

- Python 3.x
- requests: HTTP client library

## How It Works

1. **DOI Parsing**: Extracts publisher and dataset ID from DOI
2. **API Query**: Connects to Dataverse API to get dataset metadata
3. **Directory Creation**: Creates organized output directory structure
4. **Download**: Downloads complete dataset as ZIP file
5. **Extraction**: Automatically extracts ZIP contents
6. **Cleanup**: Maintains organized file structure for further processing

This tool is essential for reproducible research workflows that rely on datasets hosted in Dataverse repositories.