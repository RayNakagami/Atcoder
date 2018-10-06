N = int(input())

t = [0 for i in range(100002)]

for i in range(N):
    a,b = [int(i) for i in input().split(' ')]
    t[a-1] +=1
    t[b] -= 1

ans = 0
#print(t)
for i in range(1,100002):
    t[i] += t[i-1]
    if (t[i] >= i):
        ans = i
#print(t)
print(ans)
