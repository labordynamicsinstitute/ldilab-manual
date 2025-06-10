(help-matlab_convert_mat2csv)=

# matlab_convert_mat2csv.m - Convert MATLAB .mat files to CSV format

## Description

This script automatically converts all MATLAB data files (.mat) in the current working directory to CSV format. It extracts all variables from each .mat file and saves them as separate CSV files.

## Usage

### From within MATLAB
```matlab
>> matlab_convert_mat2csv
```

### From command line
```bash
matlab -batch "cd('path/to/mat/files'); matlab_convert_mat2csv"
```

## Input

- All .mat files in the current working directory
- .mat files should contain numeric matrices or tables

## Output

- CSV files named after the variable names within each .mat file
- Example: If `data.mat` contains variables `results` and `summary`, outputs will be `results.csv` and `summary.csv`

## Behavior

- Processes all .mat files in the current directory
- Loads each .mat file and extracts all variables
- Creates separate CSV files for each variable
- Uses variable names as CSV filenames
- Automatically exits MATLAB when complete

## Dependencies

- MATLAB with file I/O capabilities
- Read access to .mat files in current directory
- Write access to current directory for CSV output
- `writematrix` function (MATLAB R2019a or later)

## Limitations

- Only works with numeric matrices and tables
- Complex data structures may not convert properly
- Cell arrays and nested structures are not supported

## Important Note

⚠️ **Warning**: This script will exit MATLAB upon completion. Use with caution in interactive sessions.

## How It Works

1. **File Discovery**: Scans current directory for all `.mat` files
2. **File Processing**: For each `.mat` file:
   - Loads the file using `load()` function
   - Extracts all variable names using `fieldnames()`
   - For each variable, creates a CSV file named after the variable
   - Uses `writematrix()` to write numeric data to CSV
3. **Cleanup**: Automatically exits MATLAB when all conversions are complete

## Example Workflow

```bash
# Navigate to directory with .mat files
cd /path/to/data

# Run conversion (will exit MATLAB when done)
matlab -batch "matlab_convert_mat2csv"

# Results: each variable in each .mat file becomes a separate .csv file
```

## Example Output

If you have a file `experiment.mat` containing:
- Variable `data` (matrix)
- Variable `results` (table)
- Variable `metadata` (structure)

The script will create:
- `data.csv` (successfully converted)
- `results.csv` (successfully converted if numeric)
- `metadata.csv` (may fail if structure is complex)

This tool is useful for converting MATLAB data to a more portable CSV format for analysis in other tools or languages.
