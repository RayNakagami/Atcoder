N = int(input())

A = input().split(' ')

total = 0
B = [0]
dic = {}

for i in range(N):
    total += int(A[i])
    B.append(total)

for b in B:
    if b in dic:
        dic[b] +=1
    else:
        dic[b] = 1
def C(n):
    return int(n*(n-1)/2)

ans = 0;

for k,v in dic.items():
    ans += C(v)

print(ans)
