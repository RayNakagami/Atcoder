while True:
    n,m = [int(i) for i in input().split(' ')]
    if n==0:
        break
    a = [int(i) for i in input().split(' ')]
    ans =-1
    for i in range(n):
        for j in range(i+1,n):
            if a[i]+a[j] <= m:
                ans = max(ans,a[i]+a[j])

    if ans >0:
        print(ans)
    else:
        print("NONE")
