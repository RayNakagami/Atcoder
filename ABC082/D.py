N = int(input())

p = input().split(' ')
ans = 0
for i in range(N):
    if int(p[i]) == i+1:
        if not(i==N-1) and not(p[i+1] ==i+1):
            rrr = p[i]
            p[i] = p[i+1]
            p[i+1] = rrr
            ans +=1
        else:
            rrr = p[i]
            p[i]=p[i-1]
            p[i-1] =rrr
            ans +=1

print(ans)
#print(p)
