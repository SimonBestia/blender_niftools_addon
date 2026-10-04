def safe_decode(b):
    """Safely decode bytes to a string, or return as string if already one."""
    if isinstance(b, bytes):
        return b.decode("utf-8", errors="ignore")
    return str(b)
