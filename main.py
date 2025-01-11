#!/usr/bin/env python3
"""
LogAnalyzer - A simple log file analysis tool
"""

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Analyze log files')
    parser.add_argument('file', help='Log file to analyze')
    parser.add_argument('-o', '--output', help='Output format (json, csv, html)', default='json')
    
    args = parser.parse_args()
    
    print(f"Analyzing log file: {args.file}")
    print(f"Output format: {args.output}")

if __name__ == '__main__':
    main()