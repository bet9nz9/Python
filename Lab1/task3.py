from math import *
array_of_dots = [(1, 1), (4, 2), (4, 4)]

array_of_length = []

print(array_of_dots)

for i in range(0, len(array_of_dots)):
    if i == (len(array_of_dots)-1):
        array_of_length.append(sqrt((array_of_dots[0][0]-array_of_dots[i][0])**2+(array_of_dots[1][1]-array_of_dots[i][1])**2))
    else:
        array_of_length.append(sqrt((array_of_dots[i+1][0] - array_of_dots[i][0]) ** 2 + (array_of_dots[i+1][1] - array_of_dots[i][1]) ** 2))


for i in array_of_length:
    counter = 0
    for j in array_of_length:
        if i == j:
            counter += 1
    if counter == 2:
        print("Треугольник равнобедренный")
    elif counter == 3:
        print("Треугольник равносторонний")
