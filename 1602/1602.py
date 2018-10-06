def solve(lis):
    ret = 0
    for l in lis:
        


while True:
    N = int(input())
    if N==0:
        break
    lis = []
    for i in range(N):
        str = input()
        lis.append([len(str)-1,str[-1]])
    solve(lis)
