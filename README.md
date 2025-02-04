# LogAnalyzer

Simple log file analysis tool written in Python.

## Features

- Parse Apache, Nginx and generic log formats
- Generate statistics (status codes, top IPs, URLs, user agents)
- Multiple output formats: JSON, CSV, HTML
- Error detection and reporting
- Date range filtering
- Status code filtering
- IP address filtering

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
python main.py logfile.log -t nginx
python main.py logfile.log -t generic
```

Filtering options:
```bash
# Filter by date range
python main.py examples/sample.log -s --start-date 2025-01-20 --end-date 2025-01-25

# Filter by status codes (errors only)
python main.py examples/sample.log -s --status 404,500,403

# Test with nginx format
python main.py examples/nginx_sample.log -t nginx -s
```

## Options

- `-s, --stats`: Show statistics instead of raw data
- `-o, --output`: Output format (json, csv, html) - default: json
- `-t, --type`: Log format type (apache, nginx, generic) - default: apache
- `--start-date`: Filter from date (YYYY-MM-DD)
- `--end-date`: Filter to date (YYYY-MM-DD)
- `--status`: Filter by status codes (comma-separated)