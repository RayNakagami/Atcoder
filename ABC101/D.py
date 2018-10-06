def S(i):
    i=str(i)
    ret=0
    for j in i:
        ret +=int(j)
    return ret

n = 0
K=[]
for i in range(1,10**3):
    if i/S(i) >=n:
        K.append(i)
        n = i/S(i)
print(K)
for i in range(int(input())):
    print(K[i])
