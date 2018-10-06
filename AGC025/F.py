def tenTotwo(x):
    ret =""
    while x >0:
        if x%2==1:
            ret += '1'
        else:
            ret += '0'
        x //= 2

    return ret[::-1]
N,M,K = [int(i) for i in input().split(' ')]
a = input()
b = input()
a_=0
b_=0
for i in range(len(a)):
    a_ += int(a[i])*(2**(len(a)-i-1))
for i in range(len(b)):
    b_ += int(b[i])*(2**(len(b)-i-1))
#print(type(a))
for i in range(K):
    z = a_&b_
    a_ += z
    b_ += z
    #print(z)

print(tenTotwo(a_))
print(tenTotwo(b_))
