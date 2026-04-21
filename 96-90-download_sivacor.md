(help-download_sivacor)=
# download_sivacor.py - Download artifacts from SIVACOR submissions

## Description

This script downloads all artifacts from a SIVACOR submission using the SIVACOR ID stored in a Jira ticket. It handles ZIP file extraction, manages git operations, and creates a dedicated branch for the downloaded artifacts. SIVACOR (Scalable Infrastructure for Verifiable Computational Research) is a platform for executing and verifying computational reproducibility.

## Usage

```bash
python3 tools/download_sivacor.py [JIRA_CASE]
```

## Arguments

- **JIRA_CASE** (Optional) - Jira case number (e.g., "aearep-8885")

If not provided, the script determines the Jira case using this precedence:
1. Command line argument
2. Current directory name (if starts with "aearep-")
3. `jiraticket` field in config.yml

## Examples

```bash
# Using current directory name as Jira case
cd aearep-8885
python3 tools/download_sivacor.py

# Specifying Jira case explicitly
python3 tools/download_sivacor.py aearep-8885

# Using config.yml (with jiraticket field)
python3 tools/download_sivacor.py
```

## Authentication

The script requires authentication for both Jira and SIVACOR:

### Jira Authentication
- **JIRA_USERNAME** - Your Jira email address
- **JIRA_API_KEY** - API token from [Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens)

### SIVACOR Authentication
- Follow SIVACOR CLI authentication requirements (environment variables as configured by your SIVACOR setup)

## How It Works

1. **Determine Jira Case**: Identifies the Jira ticket from argument, directory name, or config.yml
2. **Lookup SIVACOR ID**: Retrieves the "SIVACOR ID" field from the Jira ticket
3. **Determine Target Folder**: Reads config.yml to find the target folder (precedence: openicpsr → zenodo → dataverse → osf)
4. **Download Artifacts**: Uses `sivacor submission get` command to download all associated files
5. **Handle ZIP Files**: If a ZIP file exists:
   - Clears the target folder contents (keeping the folder itself)
   - Unpacks the ZIP file
   - Downloads any other non-ZIP artifacts
6. **Git Operations**:
   - Creates/checks out branch: `sivacor-{sivacor_id}` (lowercase)
   - Stages the target folder
   - Commits with message: `[sivacor] Adding artifacts from SIVACOR ID {sivacor_id}`

## Config File Format

The script reads `config.yml` for target folder determination:

```yaml
openicpsr: 222222    # First priority
zenodo: 123456       # Second priority
dataverse: 789       # Third priority
osf: xyz123          # Fourth priority
jiraticket: aearep-8885  # Optional: Jira case number
```

The script uses the first non-empty value from the precedence list.

## Output Structure

### Downloaded Artifacts

```
TARGET_FOLDER/               # Determined from config.yml
├── project/                 # Extracted from ZIP (if present)
│   └── [project files]      # Replication package contents
├── stdout-{sivacor_id}      # Run output log
├── stderr-{sivacor_id}      # Run error log
└── tro/                     # Transparency and Reproducibility Objects
    ├── tro-{sivacor_id}.jsonld    # TRO Declaration
    ├── tro-{sivacor_id}.sig       # TRS Signature
    └── tro-{sivacor_id}.tsr       # Trusted Timestamp
```

### Git Branch

- **Branch Name**: `sivacor-{sivacor_id}` (lowercase, e.g., `sivacor-698e4a77bed58e3ca40df1dd`)
- **Commit Message**: `[sivacor] Adding artifacts from SIVACOR ID {sivacor_id}`

## Features

- **Automatic Jira Integration**: Pulls SIVACOR ID directly from Jira custom field
- **Smart Folder Detection**: Automatically determines target folder from config
- **ZIP Handling**: Intelligently unpacks ZIP files while preserving other artifacts
- **Git Branch Management**: Creates dedicated branches for version control
- **Error Validation**: Exits with clear errors if SIVACOR ID is not populated
- **Clean Extraction**: Clears folder before extracting to avoid file conflicts

## SIVACOR Artifacts

The script downloads several types of artifacts:

- **Replicated Package (ZIP)**: Complete replication package with execution results
- **Execution Logs**: stdout and stderr from the computational run
- **TRO Objects**: Transparency and Reproducibility metadata including:
  - JSON-LD declaration describing the computational workflow
  - Cryptographic signature for verification
  - Trusted timestamp proving execution time

## Error Handling

- **Missing SIVACOR ID**: Exits with error if Jira field is not populated
- **Invalid Jira Case**: Validates Jira case number format
- **Missing Config**: Reports if config.yml is not found or lacks repository fields
- **Download Failures**: Reports SIVACOR CLI errors with context
- **ZIP Extraction Errors**: Attempts to restore original files on failure

## Requirements

- **Python 3.x**
- **jira**: Python Jira library (for Jira API access)
- **PyYAML**: YAML configuration file support
- **sivacor**: SIVACOR CLI tool (installed via pip: `pip install sivacor`)
- **git**: Version control system

## Related Scripts

This script extends the Jira integration capabilities of:
- [jira_get_info.py](help-jira_get_info) - Retrieves information from Jira tickets
  - New keyword `sivacorid` added to support SIVACOR ID retrieval

## Workflow Integration

This script is designed to fit into the AEA replication workflow:

1. Author submits replication package
2. Package is executed on SIVACOR platform
3. SIVACOR ID is recorded in Jira "SIVACOR ID" field
4. Replicator runs this script to download verified results
5. Results are committed to a dedicated git branch
6. Replicator reviews and compares with original submission

## Security Considerations

- **Credential Storage**: Store Jira and SIVACOR credentials securely in environment variables
- **Git Operations**: Review commits before pushing to remote repositories
- **Artifact Verification**: SIVACOR provides cryptographic signatures (TRS) for artifact verification

## Troubleshooting

### "Error: SIVACOR ID field is not populated"
- Ensure the Jira ticket has the "SIVACOR ID" custom field filled in
- Verify you have the correct Jira case number

### "Error: No repository folder found in config.yml"
- Check that config.yml exists in the current directory
- Verify at least one of: openicpsr, zenodo, dataverse, or osf is specified

### SIVACOR Authentication Errors
- Verify SIVACOR CLI is properly configured
- Check environment variables required by sivacor
- Test with: `python3 -m sivacor submission list`

This tool enables seamless integration of SIVACOR-verified computational results into the AEA replication verification workflow.
