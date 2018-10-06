N = int(input())

a = [int(i) for i in input().split(' ')]

ans = 0

for a_ in a:
    while a_ %2==0:
        a_ //= 2
        ans+=1

print(ans)
