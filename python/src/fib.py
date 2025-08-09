"""
输出斐波那契数列的前20个数
"""
a, b = 0, 1

for _ in range(20):
    a, b = b, a+b
    print(a)


from functools import lru_cache

@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(i, fib1(i))