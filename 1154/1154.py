N = 300000
a = [((i % 7 ==1)or(i % 7 ==6)) for i in range(N)]
#print(a[11])
a[1]=0
p =[]
for i in range(6,N):
    if a[i]:
        p+=[i]
        for j in range(i * i ,N,i):
            a[j] = 0
 
while True:
    n = int(input())
    if n == 1:
        break
    print(n,end = ":")
    for x in p:
        if n % x ==0:
            print(" "+str(x),end = "") 

    print()
