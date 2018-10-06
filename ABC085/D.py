N,H = [int(i) for i in input().split()]
a_max = 0
b = []
for i in range(N):
    a_,b_ = [int(i) for i in input().split()]
    if a_max < a_:
        a_max = a_
    b.append(b_)

b.sort()
b  = b[::-1]
ans  = 0 
i=0
while True:
    if a_max > b[i]:
        break
    H -= b[i]
    i +=1
    ans +=1
    if H <=0 or i>=N:
        break

#print(b)
#print(ans,H,i,a_max)
if H >0:
    if H % a_max==0:
        ans += H//a_max
    else:
        ans += H//a_max +1

print(ans)
