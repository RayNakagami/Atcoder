def solve(W,H,N):
    B = [[1 for i in range(W)] for j in range(H)]
    for i in range(N):
        x,y,a =[int(j) for j in input().split(' ')]
        i
        if a==1:
            for j in range(x):
                for k in range(H):
                    B[k][j]=0
        if a==2:
            for j in range(x,W):
                for k in range(H):
                    B[k][j]=0
        if a==3:
            for j in range(y):
                B[j] =[0]*W
        if a==4:
            for j in range(y,H):
                B[j] =[0]*W
    #print(B)
    c =0
    for i in range(W):
        for j in range(H):
            if B[j][i] ==1:
                c +=1
    print(c)
W,H,N = [int(i) for i in input().split(' ')]

solve(W,H,N)
