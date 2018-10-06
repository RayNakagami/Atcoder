def solve(d,w,f):
    ans = 0
#    print("aaa")
    for i in range(d-2):
        for j in range(i+2,d):
            for k in range(w-2):
                for l in range(k+2,w):
                    minOut = 10
                    for m in range(i,j+1):
                        if minOut > f[m][k]:
                            minOut = f[m][k]
                        if minOut > f[m][l]:
                            minOut = f[m][l]
                            
                    for m in range(k,l+1):
                        if minOut > f[i][m]:
                            minOut = f[i][m]
                        if minOut > f[j][m]:
                            minOut = f[j][m]
                    total = 0
                    for m in range(i+1,j):
                        for n in range(k+1,l):
                            total += minOut-f[m][n]
                            if minOut <= f[m][n]:
                                total -= 10**5
    #                print(total,i,j,k,l)
                    if ans < total:
                        ans = total
    return ans


while True:
    d,w = [int(i) for i in input().split()]
    if d==0:
        break
    f = []
    for i in range(d):
        f.append([int(i) for i in input().split()])
    print(solve(d,w,f))

