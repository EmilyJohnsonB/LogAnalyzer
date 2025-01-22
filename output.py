import csv
import json
from io import StringIO

class OutputFormatter:
    def __init__(self):
        pass
    
    def format_json(self, data):
        """Format data as JSON"""
        return json.dumps(data, indent=2)
    
    def format_csv(self, data):
        """Format data as CSV"""
        if not data:
            return ""
        
        output = StringIO()
        
        # Handle list of entries (raw log data)
        if isinstance(data, list) and data:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        # Handle statistics dict
        elif isinstance(data, dict):
            writer = csv.writer(output)
            writer.writerow(['Metric', 'Value'])
            
            for key, value in data.items():
                if isinstance(value, dict):
                    writer.writerow([key, ''])
                    for sub_key, sub_value in value.items():
                        writer.writerow([f"  {sub_key}", sub_value])
                elif isinstance(value, list):
                    writer.writerow([key, len(value)])
                    for i, item in enumerate(value[:5]):  # Show first 5
                        writer.writerow([f"  {i+1}", str(item)])
                else:
                    writer.writerow([key, value])
        
        return output.getvalue()
    
    def format_html(self, data):
        """Format data as HTML (basic implementation)"""
        html = ["<html><head><title>Log Analysis Results</title></head><body>"]
        html.append("<h1>Log Analysis Results</h1>")
        
        if isinstance(data, list):
            html.append("<table border='1'>")
            if data:
                # Headers
                html.append("<tr>")
                for key in data[0].keys():
                    html.append(f"<th>{key}</th>")
                html.append("</tr>")
                
                # Data rows
                for entry in data:
                    html.append("<tr>")
                    for value in entry.values():
                        html.append(f"<td>{value}</td>")
                    html.append("</tr>")
            html.append("</table>")
        elif isinstance(data, dict):
            html.append("<dl>")
            for key, value in data.items():
                html.append(f"<dt><strong>{key}</strong></dt>")
                html.append(f"<dd>{value}</dd>")
            html.append("</dl>")
        
        html.append("</body></html>")
        return "\n".join(html)