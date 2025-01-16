#!/usr/bin/env python3
"""
LogAnalyzer - A simple log file analysis tool
"""

import argparse
import sys
import json
from parser import LogParser

def main():
    parser = argparse.ArgumentParser(description='Analyze log files')
    parser.add_argument('file', help='Log file to analyze')
    parser.add_argument('-o', '--output', help='Output format (json, csv, html)', default='json')
    parser.add_argument('-t', '--type', help='Log format type (apache, generic)', default='apache')
    
    args = parser.parse_args()
    
    log_parser = LogParser()
    results = []
    
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
                    
        print(f"Processed {len(results)} log entries")
        
        if args.output == 'json':
            print(json.dumps(results, indent=2))
        else:
            print("Other output formats not implemented yet")
            
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()