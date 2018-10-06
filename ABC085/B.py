N = int(input())
f = [False]*101
c = 0
for i in range(N):
    d = int(input())
    if f[d]:
        continue
    f[d] = True
    c +=1

print(c)
