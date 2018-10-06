import itertools
N,M = [int(i) for i in input().split(' ')]

x = []

for i in range(N):
    x.append([int(i) for i in input().split(' ')])
tab = [0]*N
ans = 0
#p = list(itertools.permutations(x,M));
for S in [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]:
    for j in range(N):
        a = 0
        a += x[j][0]*S[0]
        a += x[j][1]*S[1]
        a += x[j][2]*S[2]
        tab[j] = a
    tab.sort()
#    print(tab)
    a =0
    for j in range(M):
        a += tab[N-j-1]
 #   print(a)
    if a > ans:
        ans = a

#print(p)
print(ans)
   
