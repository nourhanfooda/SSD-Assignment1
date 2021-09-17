import time
import io
import contextlib
import inspect

def decorator_2(func):
    def wrapper(*args,**kwargs):
        wrapper.count += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func(*args,**kwargs)
        end = time.time()
        res = f.getvalue()
        print(f"{func.__name__} call {wrapper.count} elapsed in {end} sec")
        print("Name:    ", func.__name__)
        print("Type:    ", type(func))
        print("Sign:    ", inspect.signature(func))
        print("Args:    ", "Positional: ",locals()['args'])
        print(             "key=worded:  ",locals()['kwargs'])
        print("Doc:     ", inspect.getdoc(func))
        print("Source:  ", inspect.getsource(func))
        print("Output:  ", res)
    wrapper.count = 0
    return wrapper
