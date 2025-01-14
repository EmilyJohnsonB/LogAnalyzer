import re
from datetime import datetime

class LogParser:
    def __init__(self):
        # Common log patterns
        self.apache_pattern = re.compile(
            r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+|-)'
        )
        
    def parse_line(self, line, format_type='apache'):
        """Parse a single log line based on format type"""
        if format_type == 'apache':
            return self._parse_apache(line)
        else:
            return self._parse_generic(line)
    
    def _parse_apache(self, line):
        match = self.apache_pattern.match(line)
        if match:
            return {
                'ip': match.group('ip'),
                'timestamp': match.group('timestamp'),
                'method': match.group('method'),
                'url': match.group('url'),
                'status': int(match.group('status')),
                'size': match.group('size')
            }
        return None
        
    def _parse_generic(self, line):
        # Simple generic parser - just timestamp and message
        parts = line.split(' ', 2)
        if len(parts) >= 3:
            return {
                'timestamp': f"{parts[0]} {parts[1]}",
                'message': parts[2]
            }
        return None