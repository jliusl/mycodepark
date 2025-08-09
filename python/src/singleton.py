# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instance

#     def __init__(self, value):
#         self.value = value

# # 测试单例模式
# s1 = Singleton(10)
# s2 = Singleton(20)

# print(s1.value)  # 输出: 10
# print(s2.value)  # 输出: 10
# print(s1 is s2)  # 输出: True


# ... existing code ...

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

# 测试单例模式
s1 = Singleton(10)
s2 = Singleton(20)

print(s1.value)  # 输出: 20
print(s2.value)  # 输出: 20
print(s1 is s2)  # 输出: True

from functools import wraps
from threading import RLock

"""
单例装饰器
"""
def single(func):
    instances = {}
    lock = RLock()  # 线程锁，用于保护实例的创建

    @wraps(func)
    def wrapper(*args, **kwargs):
        if func not in instances:
            with lock:
                if func not in instances:
                    instances[func] = func(*args, **kwargs)
        return instances[func]
    return wrapper

@single
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('张三', 18)
p2 = Person('李四', 20)
print(p1 is p2)  # 输出: True
print(p1.name)  # 输出: 张三
print(p2.name)  # 输出: 张三
print(id(p1))
print(id(p2))


"""
日志装饰器, 带参数的, 可以指定日志级别
"""
def log_decorator(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'[{level}] {func.__name__} 调用成功，返回值: {result}')
            return result
        return wrapper
    return decorator

@log_decorator('DEBUG')
def calc(a, b):
    return a + b

print(calc(1, 2))