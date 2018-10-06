def solve(n):
    ans = 0
    for i in range(1,n+1):
        if n % i == 0:
            ans += 1
    return ans


for i in range(200):
    if i % 2 == 1 and solve(i)==8:
        print(i)
