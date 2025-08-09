# Apple 面试官：Sunny Jin
# 写一个函数，把输入的字符串变成驼峰字符串


s = "aaa_bbb_ccc_ddd"

def refactor(s):
    new_s = []
    for i in s.split("_"):
        new_s.append(i.capitalize())
    return " ".join(new_s)


print(refactor(s))
print(''.join([i.capitalize() for i in s.split("_")]))


