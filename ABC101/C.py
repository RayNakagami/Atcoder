N,K =[int(i) for i in input().split(' ')]

A = [int(i) for i in input().split(' ')]
"""
index_1 = -1

for i in range(len(A)):
    #print(index_1)
    if A[i]==1:
        index_1 = i
        break

ans = 0
if index_1%(K-1)==0:
    ans += index_1 // (K-1)
else:
    ans += index_1 //(K-1) + 1

if (N-index_1 -1)%(K-1)==0:
    ans += (N - index_1-1) // (K-1)
else:
    ans += (N - index_1 -1) //(K-1) + 1
    
print(ans)
"""
ans =0
if (N-1)%(K-1) ==0:
    ans = (N-1)//(K-1)
else:
    ans = (N-1)//(K-1) +1
print(ans)
