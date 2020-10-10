x = input("Enter x: ")
y = input("Enter y: ")
z = input("Enter z: ")

max = 0
min = 0

if x > (y+z):
    max = x
else:
    max = y+z

if z > x*y:
    min = z
else:
    min = x*y

print("Function: "+round(max/(1-min)))