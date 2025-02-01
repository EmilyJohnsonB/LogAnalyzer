from datetime import datetime
import re

class LogFilter:
    def __init__(self):
        # Common timestamp patterns
        self.apache_date_pattern = re.compile(r'\[([^\]]+)\]')
        
    def filter_by_date_range(self, entries, start_date=None, end_date=None):
        """Filter log entries by date range"""
        if not start_date and not end_date:
            return entries
        
        filtered = []
        for entry in entries:
            timestamp_str = entry.get('timestamp')
            if not timestamp_str:
                continue
                
            try:
                # Parse Apache/Nginx format: 23/Jan/2025:10:15:32 +0000
                if '/' in timestamp_str and ':' in timestamp_str:
                    dt = datetime.strptime(timestamp_str.split('+')[0], '%d/%b/%Y:%H:%M:%S')
                else:
                    # Try generic format
                    dt = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                
                # Check date range
                if start_date and dt.date() < start_date:
                    continue
                if end_date and dt.date() > end_date:
                    continue
                    
                filtered.append(entry)
            except ValueError:
                # Keep entries with unparseable dates
                filtered.append(entry)
        
        return filtered
    
    def filter_by_status(self, entries, status_codes):
        """Filter entries by HTTP status codes"""
        if not status_codes:
            return entries
            
        return [entry for entry in entries 
                if entry.get('status') in status_codes]
    
    def filter_by_ip(self, entries, ip_addresses):
        """Filter entries by IP addresses"""
        if not ip_addresses:
            return entries
            
        return [entry for entry in entries 
                if entry.get('ip') in ip_addresses]