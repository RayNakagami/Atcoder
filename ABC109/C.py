def gcd(a,b):
    if a%b ==0:
        if b > 0:
            return b
        else:
            return -1 * b
    return gcd(b , a % b) 

N , X = [int(i) for i in input().split()]

x = [int(i) for i in input().split()]

ret = x[0]- X

for num in x:
    ret = gcd(ret,num - X)

print(ret)
