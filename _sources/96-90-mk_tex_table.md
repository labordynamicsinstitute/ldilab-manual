(help-mk_tex_table)=

# mk_tex_table.sh - Convert standalone LaTeX table files to PDF documents

## Description

This script processes standalone LaTeX table files (.tex) and converts them to complete PDF documents. It wraps each table with a full LaTeX document structure including necessary packages for table formatting and compiles them to PDF using pdflatex.

## Usage

```bash
./mk_tex_table.sh
```

## Input

- All .tex files in the current directory (excluding those prefixed with "pdf_")
- Files should contain LaTeX table code (tabular, table, etc.)

## Output

- `pdf_{original_filename}.tex` - Complete LaTeX documents with headers
- `pdf_{original_filename}.pdf` - Compiled PDF files
- Additional LaTeX compilation files (.aux, .log, etc.)

## Behavior

- Scans current directory for .tex files
- Excludes files already prefixed with "pdf_" to avoid reprocessing
- Creates complete LaTeX documents with comprehensive package imports
- Compiles each document to PDF using pdflatex

## Packages Included

The script automatically includes these LaTeX packages for comprehensive table support:

- **inputenc**: UTF-8 encoding support
- **eurosym**: Euro symbol support
- **graphicx**: Graphics inclusion
- **geometry**: Page layout (landscape, 0.5in margins)
- **hyperref**: Hyperlink support
- **xcolor**: Color support
- **subfig**: Subfigure support
- **caption**: Enhanced captions
- **booktabs**: Professional table formatting
- **threeparttable**: Three-part table support
- **float**: Float positioning
- **adjustbox**: Box adjustments
- **supertabular**: Multi-page tables

## Dependencies

- pdflatex (TeX Live or similar LaTeX distribution)
- Standard Unix utilities (ls, grep, cat, echo)

## Example

If directory contains `results.tex` and `summary.tex`:
- Creates `pdf_results.tex` and `pdf_summary.tex` with full document structure
- Compiles to `pdf_results.pdf` and `pdf_summary.pdf`

## How It Works

1. **File Discovery**: Scans for `.tex` files, excluding those already prefixed with `pdf_`
2. **Document Creation**: For each table file:
   - Creates a complete LaTeX document with document class and package imports
   - Includes the original table content
   - Adds proper document structure (`\begin{document}` and `\end{document}`)
3. **Compilation**: Runs `pdflatex` on each complete document to generate PDF

## Page Layout

The generated documents use:
- Landscape orientation for better table viewing
- 0.5-inch margins on all sides
- Article document class

## Example Workflow

```bash
# Directory contains: table1.tex, table2.tex, summary.tex
./mk_tex_table.sh

# Results:
# - pdf_table1.tex, pdf_table1.pdf
# - pdf_table2.tex, pdf_table2.pdf  
# - pdf_summary.tex, pdf_summary.pdf
```

This tool is particularly useful for converting standalone LaTeX table fragments into viewable PDF documents for review or presentation purposes.
