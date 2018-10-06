import math
a,b = [i for i in input().split()]


c = int(a+b)

if math.sqrt(c)%1==0:
    print("Yes")
else:
    print("No")
