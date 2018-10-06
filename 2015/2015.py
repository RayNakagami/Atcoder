def solve(lis_height,lis_width):
    h=len(lis_height)
    w=len(lis_width)
    dic = {}
    for i in range(h):
        k=0
        for j in range(i,h):
            k+=lis_height[j]
            if k in dic:
                dic[k]+=1
            else:
                dic[k]=1
    ans = 0
    #print(dic)
    #print(w,'a')
    for i in range(w):
        k=0
        for j in range(i,w):
            k+=lis_width[j]
           # print(j)
            if k in dic:
                ans += dic[k]
                #print(k,dic[k])

    print(ans)


while True:
    h,w=[int(i) for i in input().split(' ')]
   # print(a)
    if h == 0:
        break
    lis_h =[]
    lis_w=[]
    for i in range(h):
        lis_h.append(int(input()))
    for i in range(w):
        lis_w.append(int(input()))

    solve(lis_h,lis_w)
