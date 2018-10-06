C,D = [int(i) for i in input().split()]

ans = 0
low = 140
high = 170

while high < C:
    low *= 2
    high *= 2

while True:
    l = max(low,C)
    if D <= high:
        if D > low:
            ans += D - l
        break
    else:
        ans += high - l

    low *= 2
    high *= 2

print(ans)
