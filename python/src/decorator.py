import time
from functools import wraps

def timeing(unit: str):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            print(f'Elapsed time: {elapsed:.2f}{unit}')
            return result
        return wrapper
    return decorator


@timeing("秒")
def test(n: int) -> None:
    time.sleep(n)

test(3)
