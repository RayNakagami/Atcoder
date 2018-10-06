def gcd(a,b):
    if a % b ==0:
        return b
    return gcd(b,a%b)

N = int(input())
a = 1
for i in range(N):
    b = int(input())
    a = a * b // gcd(a,b)

print(a)
