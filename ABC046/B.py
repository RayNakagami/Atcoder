i = input().split(' ')

N = int(i[0])
K = int(i[1])

ans = K

for i in range(N-1):
    ans *= (K-1)

print(ans)
