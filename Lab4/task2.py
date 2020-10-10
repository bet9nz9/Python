def is_simple(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num

def print_geminy(array_of_nums):
    previous_num = arr_of_simple_nums[0]
    for num in arr_of_simple_nums:
        if  (num - previous_num) == 2:
            print("Geminy numbers: "+str(previous_num)+" "+str(num))
        previous_num = num

arr_of_simple_nums = []
for num in range(2, 200):
    if  is_simple(num):
        arr_of_simple_nums.append(num)

print_geminy(arr_of_simple_nums)