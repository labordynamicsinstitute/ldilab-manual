(help-matlab_convert_fig)=

# matlab_convert_fig.m - Convert MATLAB .fig files to PNG format

## Description

This script automatically converts all MATLAB figure files (.fig) in the current working directory to PNG format. It preserves the original filename and creates corresponding .png files.

## Usage

### From within MATLAB
```matlab
>> matlab_convert_fig
```

### From command line
```bash
matlab -batch "cd('path/to/fig/files'); matlab_convert_fig"
```

## Input

- All .fig files in the current working directory

## Output

- PNG files with the same base filename as the original .fig files
- Example: `figure1.fig` → `figure1.png`

## Behavior

- Processes all .fig files in the current directory
- Opens each figure file and saves it as PNG
- Handles multiple figures within a single .fig file
- Automatically exits MATLAB when complete

## Dependencies

- MATLAB with figure handling capabilities
- Read access to .fig files in current directory
- Write access to current directory for PNG output

## Important Note

⚠️ **Warning**: This script will exit MATLAB upon completion. Use with caution in interactive sessions.

## How It Works

1. **File Discovery**: Scans current directory for all `.fig` files
2. **File Processing**: For each `.fig` file:
   - Opens the figure using `openfig()`
   - Extracts the base filename without extension
   - Saves each figure in the file as PNG using `saveas()`
3. **Cleanup**: Automatically exits MATLAB when all conversions are complete

## Example Workflow

```bash
# Navigate to directory with .fig files
cd /path/to/figures

# Run conversion (will exit MATLAB when done)
matlab -batch "matlab_convert_fig"

# Results: all .fig files converted to .png
```

This tool is particularly useful for batch conversion of MATLAB figures to a more portable PNG format for inclusion in reports or presentations.
