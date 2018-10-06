N = 10**6

N1 = [i for i in range(N+40)]
N2 = [i for i in range(N+40)]

#N1[0] = 0
#N2[0] = 0

p = [n*(n+1)*(n+2)//6 for n in range(1,200) if n *(n+1)*(n+2)//6< N+1]
p2 = [n*(n+1)*(n+2)//6 for n in range(1,200) if n *(n+1)*(n+2)//6< N+1 and n *(n+1)*(n+2)//6 % 2 ==1 ]
#print(p2)
for p_ in p:
    if p_ > N +1:
        continue
    n = min(p_*5,N)
    for j in range(p_,n):
#        print(j)
        if N1[j] > N1[j-p_] +1:
            N1[j] = N1[j-p_]+1
print("a")
for p_ in p2:
    if p_ > N +1 :
        continue
    #n = min(p_*7,N+1)
    for j in range(p_,N):
        if N2[j] > N2[j-p_]+1:
            N2[j] = N2[j -p_]+1
#print('a')
while True:
    n = int(input())
    if n == 0:
        break
    print(N1[n],N2[n])
