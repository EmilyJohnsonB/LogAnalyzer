from collections import defaultdict, Counter

class LogAnalyzer:
    def __init__(self):
        pass
    
    def analyze_entries(self, entries):
        """Analyze a list of parsed log entries"""
        stats = {
            'total_entries': len(entries),
            'status_codes': defaultdict(int),
            'ips': Counter(),
            'methods': Counter(),
            'urls': Counter(),
            'errors': []
        }
        
        for entry in entries:
            # Apache format analysis
            if 'status' in entry:
                stats['status_codes'][entry['status']] += 1
                if entry['status'] >= 400:
                    stats['errors'].append({
                        'line': entry.get('line_number'),
                        'status': entry['status'],
                        'url': entry.get('url'),
                        'ip': entry.get('ip')
                    })
            
            if 'ip' in entry:
                stats['ips'][entry['ip']] += 1
                
            if 'method' in entry:
                stats['methods'][entry['method']] += 1
                
            if 'url' in entry:
                stats['urls'][entry['url']] += 1
        
        # Convert to regular dict for JSON serialization
        stats['status_codes'] = dict(stats['status_codes'])
        stats['top_ips'] = dict(stats['ips'].most_common(10))
        stats['top_urls'] = dict(stats['urls'].most_common(10))
        stats['methods'] = dict(stats['methods'])
        
        # Remove counters to avoid serialization issues
        del stats['ips']
        del stats['urls']
        
        return stats