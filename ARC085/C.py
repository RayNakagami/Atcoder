N,M=[int(i) for i in input().split()]

ans = (M*1900 +(N-M)*100)* 2**M

print(ans)
