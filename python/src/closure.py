def make_person(name):
    def greet():
        return f"Hello, I'm {name}!"
    
    def change_name(new_name):
        nonlocal name
        name = new_name
    
    return greet, change_name

# 创建一个"人"
greet, change_name = make_person("Alice")
print(greet())  # Hello, I'm Alice!

change_name("Bob")
print(greet())  # Hello, I'm Bob!（状态已更新）
