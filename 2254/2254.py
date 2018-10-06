import itertools

def solve(lis,N):
    ans_=10000
    c_time =[10000]*N
    n_lis = list(range(N))
    for com in itertools.permutations(n_lis):
        ans =0
        for i in range(N):
            c_time[i]=lis[i][0]
        for i in com:
            ans += c_time[i]
            for j in range(N):
                c_time[j] =min(c_time[j],lis[i][j+1])
        
#        print(c_time)
        if ans_ >ans:
            ans_=ans

    print(ans_)

while True:
    N = int(input())
    if N==0:
        break
    lis =[]
    for i in range(N):
        lis.append([int(i) for i in input().split(' ')])

    solve(lis,N)
