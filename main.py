#!/usr/bin/env python3
"""
LogAnalyzer - A simple log file analysis tool
Version: 1.0.0
"""

__version__ = "1.0.0"

import argparse
import sys
import json
from datetime import datetime
from parser import LogParser
from analyzer import LogAnalyzer
from output import OutputFormatter
from filters import LogFilter
from utils import get_file_size_mb, suggest_batch_size

def main():
    parser = argparse.ArgumentParser(description='Analyze log files')
    parser.add_argument('file', help='Log file to analyze')
    parser.add_argument('-o', '--output', help='Output format (json, csv, html)', default='json')
    parser.add_argument('-t', '--type', help='Log format type (apache, nginx, generic)', default='apache')
    parser.add_argument('-s', '--stats', action='store_true', help='Show statistics instead of raw data')
    parser.add_argument('--start-date', help='Filter from date (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='Filter to date (YYYY-MM-DD)')
    parser.add_argument('--status', help='Filter by status codes (comma-separated)', type=str)
    parser.add_argument('--batch-size', help='Process file in batches (for large files)', type=int, default=1000)
    parser.add_argument('--version', action='version', version=f'LogAnalyzer {__version__}')
    
    args = parser.parse_args()
    
    log_parser = LogParser()
    results = []
    
    # Check file size and suggest batch size
    file_size_mb = get_file_size_mb(args.file)
    if file_size_mb > 1 and args.batch_size == 1000:
        suggested = suggest_batch_size(file_size_mb)
        print(f"File size: {file_size_mb:.1f}MB. Consider using --batch-size {suggested} for better performance.", file=sys.stderr)
    
    try:
        with open(args.file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                    
                parsed = log_parser.parse_line(line, args.type)
                if parsed:
                    parsed['line_number'] = line_num
                    results.append(parsed)
                
                # Progress indicator for large files
                if line_num % args.batch_size == 0:
                    print(f"Processing... {line_num} lines processed", file=sys.stderr)
                    
        # Apply filters
        log_filter = LogFilter()
        
        # Date filtering
        start_date = None
        end_date = None
        if args.start_date:
            start_date = datetime.strptime(args.start_date, '%Y-%m-%d').date()
        if args.end_date:
            end_date = datetime.strptime(args.end_date, '%Y-%m-%d').date()
            
        results = log_filter.filter_by_date_range(results, start_date, end_date)
        
        # Status code filtering  
        if args.status:
            status_codes = [int(s.strip()) for s in args.status.split(',')]
            results = log_filter.filter_by_status(results, status_codes)
                    
        print(f"Processed {len(results)} log entries (after filtering)")
        
        formatter = OutputFormatter()
        
        if args.stats:
            analyzer = LogAnalyzer()
            stats = analyzer.analyze_entries(results)
            output_data = stats
        else:
            output_data = results
        
        if args.output == 'json':
            print(formatter.format_json(output_data))
        elif args.output == 'csv':
            print(formatter.format_csv(output_data))
        elif args.output == 'html':
            print(formatter.format_html(output_data))
        else:
            print(f"Unknown output format: {args.output}")
            
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()