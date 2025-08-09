sentence = input("输入一段数字与字母的混合：")
counter = {}
for i in sentence:
    if i.isdigit():
        counter[i] = counter.get(i, 0) + 1
sorted_keys = sorted(counter, key=lambda x: counter[x], reverse=True)
for key in sorted_keys:
    print(f'{key} 出现了 {counter[key]}次')