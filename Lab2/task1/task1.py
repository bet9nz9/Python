import random

numbers_file = open("numbers.txt", "w")

for i in range(0, 20):
    number = ""
    for j in range(0, 3):
        number += str(random.randint(0, 9))
    numbers_file.write(number+"\n")

numbers_file.close()

numbers_file = open("numbers.txt", "r")
arr_of_numbers = numbers_file.readlines()
numbers_file.close()

arr_of_final_nums = []
for num in arr_of_numbers:
    sum_of_nums = int(num[0])+int(num[1])+int(num[2])
    mul_of_nums = int(num[0])*int(num[1])*int(num[2])
    if sum_of_nums == mul_of_nums:
        arr_of_final_nums.append(num)

# print(len(arr_of_final_nums))
final_nums_file = open("final.txt", "w")

if len(arr_of_final_nums) == 0:
    final_nums_file.write("0\n")
else:
    for i in final_nums_file:
        final_nums_file.write(str(i)+"\n")

def get_sum_of_nums(array_of_nums):
    sum_of_nums = 0
    for i in array_of_nums:
        sum_of_nums += int(i)
    return sum_of_nums

final_nums_file.write("Сумма всех чисел: "+str(get_sum_of_nums(arr_of_final_nums)))

