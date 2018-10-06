N = int(input())

a = [int(i) for i in input().split()]
b = -1
count = 0
ans = 0
for a_ in a:
    if b == a_:
        count += 1
    else:
        ans += count //2
        count = 1
    b = a_

ans += count //2
print(ans)
