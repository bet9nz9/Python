import math
# for i in range(-1.0, 0.0, 0.1):
#     print(str(i) + "\t" + "y = " + str((-2.0 * (i ** 2.0) - (2.0*i) + 1.0)))

i = -1.0
while math.ceil(i) <= 0:
    print(str(i) + "\ty = " + str((-2.0 * (i ** 2.0) - (2.0*i) + 1.0)))
    i += 0.1
