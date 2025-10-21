# docmd

`docmd` (Document Merge & Dump) is a simple command-line tool to merge the contents of multiple source files into a single text document.

## Installation

```bash
pip install git+https://github.com/brunardo19/docmd.git
```

Requires Python 3.7 or higher and git

## Usage

```bash
docmd --help
```

This will display the following output, which serves as a complete reference:

```text
usage: docmd [-h] [-s SOURCE] [-e EXT [EXT ...]] [-o OUTPUT]

Combine files with specific extensions into one output file.

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source directory (default: current working directory)
  -e EXT [EXT ...], --ext EXT [EXT ...]
                        File extension(s) to search for, without the dot
                        (e.g., md py txt). (default: md)
  -o OUTPUT, --output OUTPUT
                        Output file path (default: combined_{first_ext}.txt)
```
