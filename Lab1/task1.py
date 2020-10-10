# Задача 1

num1 = input('Enter num1: ')
num2 = input('enter num2: ')

arr = []

for i in range(0, len(num2)):
    for j in range(0, len(num2)):
        for g in range(0, len(num2)):
            arr.append(num2[i]+num2[j]+num2[g])

if num1 in arr:
    print("ok")
else:
    print('not ok')
