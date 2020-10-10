import random
import math

num = random.uniform(-2, 2)

if num < 0:
    print("Num = "+str(num)+"\t fun: "+str(math.cos(num)))
elif num >= 0 and num < 1.5:
    print("Num = "+str(num)+"\t fun: "+str(num**3 + 2*num**2 +1))
else:
    print(str(0))
