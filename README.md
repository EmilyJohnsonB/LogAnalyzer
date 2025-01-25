# LogAnalyzer

Simple log file analysis tool written in Python.

## Features

- Parse Apache and generic log formats
- Generate statistics (status codes, top IPs, URLs)
- Multiple output formats: JSON, CSV, HTML
- Error detection and reporting

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python main.py examples/sample.log
```

Show statistics instead of raw data:
```bash
python main.py examples/sample.log -s
```

Different output formats:
```bash
python main.py examples/sample.log -s -o csv
python main.py examples/sample.log -s -o html
```

Log format types:
```bash
python main.py logfile.log -t apache
python main.py logfile.log -t generic
```

## Options

- `-s, --stats`: Show statistics instead of raw data
- `-o, --output`: Output format (json, csv, html) - default: json
- `-t, --type`: Log format type (apache, generic) - default: apache