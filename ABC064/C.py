def color(s):
    if s < 400:
        return 0
    if s < 800:
        return 1
    if s < 1200:
        return 2
    if s < 1600:
        return 3
    if s < 2000:
        return 4
    if s < 2400:
        return 5
    if s < 2800:
        return 6
    if s < 3200:
        return 7
    return 8


N = int(input())

a = [color(int(i)) for i in input().split()]
ans = 0
table = [False for i in range(10)]
for i in a:
    if i == 8:
        ans += 1
    else:
        table[i] = True

ret = 0
for f in table:
    if f:
        ret += 1

ans1 = max(ret,1)
ans2 = min(ret+ans,8)

print(ans1,ans2)
