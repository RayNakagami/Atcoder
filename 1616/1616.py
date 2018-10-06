while True:
    n,m=[int(i) for i in input().split()]
    if n==0:
        break 
    a = [int(i) for i in input().split()]

    ans  = -1
    for i in range(n):
        for j in range(i+1,n):
            if a[i]+a[j] <= m:
                ans =max(a[i]+a[j] ,ans)
    if ans ==-1:
        print("NONE")
    else:
        print(ans)
