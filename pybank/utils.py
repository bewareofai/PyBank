from .exceptions import BankError
def log_operation(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print (f"[LOG] {func.__name__} -> OK")
            return result
        except BankError as e:
            print (f"[LOG] {func.__name__} -> {type(e).__name__}")
            raise
    return wrapper


