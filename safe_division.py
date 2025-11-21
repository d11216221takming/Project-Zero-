def safe_division(a, b):
    """
    Safely divides a by b. Returns None if b is zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None
