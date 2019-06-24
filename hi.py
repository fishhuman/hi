name = input('請輸入名字: ')
print('嗨', name)

height = input('請輸入身高: ')
weight = input('請輸入體重: ')


bmi = float(weight)/((float(height)/100)**2)

print('你的BMI值為: ', bmi )