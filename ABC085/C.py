def solve(N,Y):
    Y //= 1000
    for i in range(Y//10+1):
#        print(Y-N-9*i)
        if (Y - N -9*i)%4==0:
            b = (Y-N-9*i)//4
            if N-i-b >= 0 and b >=0:
                return [i,b,N-i-b]
    
    return [-1,-1,-1]


N,Y=[int(i) for i in input().split()]

lis = solve(N,Y)

print(lis[0],lis[1],lis[2])

