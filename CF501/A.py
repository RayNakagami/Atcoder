n,m = [int(i) for i in input().split()]

table = [True for i in range(105)]
table[0] = False

for i in range(n):
    l,r = [int(i) for i in input().split()]
    for j in range(l,r+1):
        table[j] = False

ans = 0
t = []
for i in range(m):
    if table[i]:
        ans += 1
        t.append(i)

print(ans)
for i in t:
    print(i,end = ' ')
print()
