year = int(input("请输入年份："))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f"{year}年是闰年" if is_leap else f"{year}年不是闰年")