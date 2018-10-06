a,b,x = [int(i) for i in input().split(' ')]
ans = b//x - a//x
if a%x==0:
    ans +=1
    """
if a%x==0:
    ans +=1
"""
print(ans)
