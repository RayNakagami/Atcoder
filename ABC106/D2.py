N , M , Q = [int(i) for i in input().split()]
table = [[0 for j in range(N)] for i in range(N)]

for i in range(M):
    L,R = [int(char) for char in input().split()]
    table[L-1][R-1] += 1

for i in range(Q):
    p,q = [int(char) for char in input().split()]
    ans = 0
    for j in range(p-1,q):
        for k in range(j,q):
            ans += table[j][k]
    print(ans)
