x = input("Enter x coordinate of dot: ")
y = input("Enter y coordinate of dot: ")

if x >= -2 and x <= 0:
    if y >= 0 and y <= 2:
        print("The point is in the area.")
elif x >= 0 and x <= 2:
    if y <= 0 and y >= -2:
        print("The point is the area.")
else:
    print("The point is't in the area.")