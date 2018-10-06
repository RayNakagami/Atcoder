lis = input().split(' ')
N= int(lis[0])
L = int(lis[1])

l = input().split(' ')
for i in range(N):
    l[i] = int(l[i])
l.sort()

#print(l)
ans = 0
n = N - 1
for i in range(L):
#    print(l[n])
    ans += l[n]
    n -= 1

print(ans)
