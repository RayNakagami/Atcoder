N,x = [int(i) for i in input().split(' ')]

a = [int (i) for i in input().split(' ')]
ans =0
if a[0] > x:
    ans += a[0]-x
    a[0]=x
for i in range(N-1):
    if a[i]+a[i+1] > x:
        ans += (a[i]+a[i+1])-x
        a[i+1] -= (a[i]+a[i+1])-x

print(ans)
