INF = 1000000

dp = [INF for i in range(100040)]

dp[0]= 0

a = [1]
n = 6
while True:
    a.append(n)
    n *= 6
    if n > 100000:
        break
n= 9
while True:
    a.append(n)
    n *= 9
    if n > 100000:
        break
a.sort()
for i in range(len(a)):
    a_ =  a[i]
    for j in range(a[i],len(dp)):
        dp[j] = min(dp[j],dp[j-a_] + 1)

print(dp[int(input())])
