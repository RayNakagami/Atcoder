N,x = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]
total = 0
for  a_ in a:
    total  += a_
a.sort()
c = 0
if total > x:
    i = 0
    while(True):
        x -= a[i]
        i+=1
        if x < 0:
            print(c)
            break
        c +=1
elif total < x:
    print(N-1)

else:
    print(N)
