n,m,d = [int(i) for i in input().split()]
if d == 0:
    ans = (n-d)*(m-1)/(n*n)
else:
    ans = 2*(n-d)*(m-1)/(n*n)

print(ans)
