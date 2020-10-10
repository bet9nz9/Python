num = int(input("Enter a Num of nums: "))
arr_of_nums = []
for i in range(0, num):
    arr_of_nums.append(int(input("Enter a num: ")))

trigger = False
for i in arr_of_nums:
    if i < 0:
        trigger = True
if trigger:
    print("There are negative nums in collection")
else:
    print("All nums is positive")