arr_of_perfect_nums = []

for i in range(1, 1000000):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        arr_of_perfect_nums.append(i)
        print(str(i))

print(len(arr_of_perfect_nums))

for i in arr_of_perfect_nums:
    print(str(i))
