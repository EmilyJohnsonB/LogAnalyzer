import os

def get_file_size_mb(filepath):
    """Get file size in megabytes"""
    size_bytes = os.path.getsize(filepath)
    return size_bytes / (1024 * 1024)

def format_number(num):
    """Format large numbers with commas"""
    return f"{num:,}"

def suggest_batch_size(file_size_mb):
    """Suggest optimal batch size based on file size"""
    if file_size_mb < 1:
        return 1000
    elif file_size_mb < 10:
        return 5000  
    elif file_size_mb < 100:
        return 10000
    else:
        return 25000