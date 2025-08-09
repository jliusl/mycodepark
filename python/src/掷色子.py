import random

# 使用列表来存储每个点数出现的次数，索引 0 到 5 分别对应点数 1 到 6
counts = [0] * 6

for _ in range(1000):
    # 修正随机数范围为 1 到 6
    num = random.randint(1, 6)
    # 因为列表索引从 0 开始，所以用 num - 1
    counts[num - 1] += 1

# 循环打印每个点数出现的次数
for i in range(6):
    print(f"{i + 1}出现了{counts[i]}次")
