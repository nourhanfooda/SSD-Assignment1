import time
import io
import contextlib

def decorator_1(func):
    def wrapper(*args,**kwargs):
        wrapper.count += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func(*args,**kwargs)
        end = time.time()
        res = f.getvalue()
        print(f"{func.__name__} call {wrapper.count} elapsed in {end} sec")
    wrapper.count = 0
    return wrapper