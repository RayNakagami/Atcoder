import math
N = int(input())
def ceil(x,y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1
t=1
a=1
for i in range(N):
    T , A = [int(i) for i in input().split(' ')]
 #   print(T,A)
    n1 = ceil(t , T)
    n2 = ceil(a , A)
    n = max(n1,n2)
    #while T*n <= t and A*n <= a:
     #   n += 1
    
    t = T*n
    a = A*n
#    print(t,a)

print(t+a)
