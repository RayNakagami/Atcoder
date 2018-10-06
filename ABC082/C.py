X = [0 for i in range(10**5+40)]

n = int(input())

a = input().split(' ')

for a_ in a:
    a_ = int(a_)
    for i in [-1,0,1]:
        X[a_ + i] +=1
print(max(X))
