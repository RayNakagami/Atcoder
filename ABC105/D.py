import math

N , M = [int(i) for i in input().split()]
lis = {}
lis[0] = 1
now = 0
for i in input().split():
    now += int(i)
    now %= M
    if now  in lis:
        lis[now % M] +=1
    else:
        lis[now % M] = 1

ans = 0
for i in lis.values():
    ans += i * (i - 1) // 2

print(ans)
#print(lis)
