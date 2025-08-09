import threading


class singlemeta(type):


    def __init__(cls, *args, **kwargs):
        cls._instance = None
        cls._lock = threading.RLock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
    

class Employee(metaclass=singlemeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age


e1 = Employee("张三", 18)
e2 = Employee("李四", 20)
print(e1.name)
print(e2.name)
print(e1 is e2)