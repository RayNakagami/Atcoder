D,N = [int(i) for i in input().split(' ')]
"""
ans = 100**D
ans *= N
print(ans)
"""
if N >= 100:
    N +=1
print(N,end="")
for i in range(D):
    print("00",end ="")

print()
