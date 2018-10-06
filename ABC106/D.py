N , M , Q = [int(i) for i in input().split()]
L = [0 for i in range(N)]
R = [0 for i in range(N)]
for i in range(M):
    L_ , R_ = [int(char) for char in input().split()]

    L[L_-1] += 1
    R[R_-1] += 1
L1 = [0 for i in range(N)]
R1 = [0 for i in range(N)]

for i in range(N-1):
    L1[i+1] = L1[i] + L[i]
    R1[-(i+1)-1] = R1[-i-1] + R[-i-1]

print(L1,R1)
for i in range(Q):
    p , q = [int(char) for char in input().split()]
    ans = M - max(L1[p-1],R1[q-1])
    print(ans)
