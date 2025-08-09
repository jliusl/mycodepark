import time
from functools import wraps

def timeing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f'Elapsed time: {elapsed:.2f}s')
        return result
    return wrapper

@timeing
def test(n: int) -> None:
    time.sleep(n)

test(3)
