from functools import wraps
import time



def Single(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        start = time.time()
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        end = time.time()
        print(f'耗时：{end - start:..2f}')
        return instances[cls]
    return wrapper

@Single
class Foo():
    pass


