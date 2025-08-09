height = float(input("输入身高(cm): "))
weight = float(input("输入体重(kg): "))

bmi = weight / (height / 100) ** 2
if bmi < 18.5:
    print("体重过轻")
elif bmi < 24:
    print("正常体重")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
print(f"您的BMI值为: {bmi:.2f}")
