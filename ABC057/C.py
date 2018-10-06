import math
N = int(input())

n = int(math.sqrt(N))+1
#print(n)
def digit(x):
    if 1 <= x < 10:
        return 1
    elif x < 100:
        return 2
    elif x < 1000:
        return 3
    elif x < 10000:
        return 4
    elif x < 100000:
        return 5
    elif x < 1000000:
        return 6
    elif x < 10000000:
        return 7
    elif x < 100000000:
        return 8
    elif x < 1000000000:
        return 9
    else:
        return 10

while True:
    if(N % n == 0):
        k = N / n
        print(digit(k))
        break
    n-=1
