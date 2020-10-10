# Задача 2

num = input("Enter num of element(num>=1 and num <= 180): ")
if int(num) >= 1 and int(num) <= 180:
    sequenceOfNums = str()

    for i in range(10, 100):
        sequenceOfNums += str(i)

    if int(num) == 1:
        print(sequenceOfNums[0])
    elif int(num) == 180 :
        print(sequenceOfNums[179])
    else:
        print(sequenceOfNums[int(num)])
else:
    print("Your num is not in range.")

# sequenceOfNums = str()
#
# for i in range(10, 100):
#     sequenceOfNums += str(i)
#
# print(sequenceOfNums)
