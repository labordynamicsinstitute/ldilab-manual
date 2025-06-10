(help-generate_png_diff)=

# generate_png_diff.sh - Generate visual diffs for modified PNG images

## Description

This script compares PNG images in the git repository that have been modified against their original versions (from HEAD). It generates visual difference images and calculates Mean Absolute Error (MAE) statistics for each comparison.

## Usage

```bash
./generate_png_diff.sh [modified_dir]
```

## Parameters

- **modified_dir** - Directory containing the modified images (optional)
  - Default: "209827/local/LocalOutputs"

## Output Files

- `{modified_dir}/diffs/diff_{image_name}.png` - Visual diff images
- `generated/image_diff_stats.txt` - Summary statistics file
- `generated/image_diff_stats.txt.raw` - Detailed comparison output

## Dependencies

- ImageMagick (magick command with composite and compare tools)
- Git (for retrieving original images and detecting changes)

## Examples

```bash
# Use default directory
./generate_png_diff.sh

# Use custom directory
./generate_png_diff.sh "custom/output/directory"
```

## How It Works

1. **File Discovery**: Scans git for modified PNG files using `git diff --name-only HEAD`
2. **Image Extraction**: Retrieves original images from git HEAD into temporary files
3. **Visual Diff Generation**: Uses ImageMagick's composite tool with difference mode to create visual diffs
4. **Statistical Analysis**: Calculates Mean Absolute Error (MAE) using ImageMagick's compare tool
5. **Output Generation**: Creates summary statistics and detailed comparison logs

## Output Format

The script generates two types of output files:

- **Summary file** (`image_diff_stats.txt`): Contains filename and MAE value for each image
- **Raw file** (`image_diff_stats.txt.raw`): Contains detailed ImageMagick compare output

Visual difference images are saved in the `{modified_dir}/diffs/` directory with the prefix `diff_`.
