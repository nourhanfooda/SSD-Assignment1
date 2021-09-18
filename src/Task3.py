import time
import io
import contextlib
import inspect
import logging
import pandas as pd

class decorator_3:
    global result, dict
    result = []
    dict = {}
    def __init__(self,func):
        self.func = func
        self.count = 0

    def __call__(self,*args,**kwargs):
        def Sort_sub(sub_lst):
            sub_lst.sort(key=lambda x: x[1])
            return sub_lst

        def insert_second(lst,i):
            lst.insert(1,i)
            return lst

        self.count += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            self.func(*args,**kwargs)
        end = time.time()
        res = f.getvalue()
        if self.func.__name__ in dict:
            return
        else:
            dict[self.func.__name__] = end

        if len(dict) == 4:
            result = [[k,v] for k,v in dict.items()]
            final = Sort_sub(result)
            rank = [insert_second(j,i+1) for i,j in enumerate(result)]
            df = pd.DataFrame(rank,columns=["functionName", "Rank","Time"])
            print(df)

        with open("output.txt", "a") as f:
            print(f"{self.func.__name__} call {self.count} elapsed in {end} sec", file=f)
            print("Name:    ", self.func.__name__, file=f)
            print("Type:    ", type(self.func), file=f)
            print("Sign:    ", inspect.signature(self.func), file=f)
            print("Args:    ", "Positional: ",locals()['args'], file=f)
            print(             "key=worded:  ",locals()['kwargs'], file=f)
            print("Doc:     ", inspect.getdoc(self.func), file=f)
            print("Source:  ", inspect.getsource(self.func), file=f)
            print("Output:  ", res, file=f)
