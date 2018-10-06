dic = {}

N,K = [int(i) for i in input().split()]

dic = {}

for i in range(N):
    a,b = [int(i) for i in input().split()]
    if a in dic:
        dic[a] += b
    else:
        dic[a] = b


ans = sorted(dic.items())

for i,j in ans:
    K -= j
    if K <= 0:
        print(i)
        break

