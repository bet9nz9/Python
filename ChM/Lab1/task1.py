x = input('Enter x value: ')

def first(x):
    result = 5+(6/(7+int(x)))
    return result

def second(first_result):
    return 3+(4/first_result)

def third(second_result):
    return 1+(2/second_result)

if int(x) != -7 :
    first_result = first(x)
    if first_result != 0:
        second_result=second(first_result)
        if second_result != 0:
            print('Result = '+str(third(second_result)))
        else:
            print("Error, division by 0!")
    else:
        print("Error, division by 0!")
else:
    print("Error, division by 0!")
