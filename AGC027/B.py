N,X = [int(i) for i in input().split()]


x = [int(i) for i in input().split()]
x.insert(0,0)
x.reverse()
table = [[0 for i in range(N+5)]for j in [0,1] ]

table[0][0] = 0
a = False
for i in range(N):
    for j in range(i):
       table[not(a)][j+1] = table[a][j] + (j+2)*(j+2)*(x[j] - x[j+1]) + X
    table[not(a)][0] = table[a][i-1] + (i+1)*(i+1)*x[i-1] + x[i] + X
    
    a = not(a)

ans = 10000000000000000
for i in range(N):
    ans = min(ans, table[a][i] + (i+2)*(i+2) * x[N-1] + X)
print(ans)
