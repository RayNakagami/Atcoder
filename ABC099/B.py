a , b = [int(i) for i in input().split(' ')]

dif = b - a
ans = dif * (dif + 1) // 2 - b

print(ans)
