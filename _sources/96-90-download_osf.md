(help-download_osf)=

# download_osf.sh - Download files from Open Science Framework (OSF) projects

## Description

This script downloads all files and directories from an OSF project using the osfclient command-line tool. It's designed for replication workflows where researchers need to download datasets, code, and other materials from OSF repositories for analysis and verification.

## Usage

```bash
./download_osf.sh <OSF_DOI_OR_PROJECT_ID>
bash tools/download_osf.sh <OSF_DOI_OR_PROJECT_ID>
```

## Arguments

- **OSF_DOI_OR_PROJECT_ID** - OSF project identifier, can be:
  - Project ID (e.g., "abc12")
  - Full OSF URL (e.g., "https://osf.io/abc12/")
  - OSF DOI (e.g., "10.17605/OSF.IO/ABC12")

## Examples

```bash
# Using project ID directly
./download_osf.sh abc12

# Using full OSF URL
./download_osf.sh https://osf.io/abc12/

# Using OSF DOI
./download_osf.sh 10.17605/OSF.IO/ABC12
```

## Requirements

- **osfclient**: OSF command-line client (`pip install osfclient`)
- Internet connection to access OSF API
- Read/write permissions in current directory

## Features

- Flexible input parsing (accepts URLs, DOIs, or project IDs)
- Creates organized directory structure: `osf-[PROJECT_ID]`
- Downloads complete project structure including subdirectories
- Preserves original file organization and metadata
- Validates osfclient installation before proceeding

## Behavior

- Extracts project ID from various input formats
- Creates target directory named "osf-[PROJECT_ID]"
- Downloads all files using osfclient's clone command
- Maintains original directory structure from OSF
- Exits with error if osfclient is not installed

## Output Structure

```
Input: abc12 (or https://osf.io/abc12/ or DOI)
Output directory: ./osf-abc12/
Contents: Complete OSF project structure with all files and subdirectories
```

## Error Handling

- Validates command-line arguments (requires exactly one argument)
- Checks for osfclient installation before proceeding
- Reports download failures from osfclient
- Provides clear error messages for common issues

## Dependencies

### osfclient installation:
```bash
pip install osfclient
# or
pip install -r requirements.txt  # if included in project requirements
```

## OSF API

- Uses osfclient which interfaces with OSF's REST API
- Works with public projects (no authentication required for public data)
- Supports downloading complete project hierarchies
- Preserves file metadata and timestamps

## How It Works

1. **Input Parsing**: Extracts project ID from URLs, DOIs, or direct IDs
2. **Validation**: Checks for osfclient installation and valid arguments
3. **Directory Creation**: Creates organized output directory
4. **Download**: Uses osfclient's clone command to download entire project
5. **Organization**: Maintains original OSF project structure

## Authentication

For private OSF projects, you may need to set up authentication:
```bash
osf auth
```

This tool is essential for reproducible research workflows that rely on datasets and materials hosted in OSF repositories.