N,K = [int(i) for i in input().split()]

x = [int(i) for i in input().split()]

plus = [0]
minus = [0]

for x_ in x:
    if x_ < 0:
        minus.append(x_ * -1)
    if x_ > 0:
        plus.append(x_)
    if x_ == 0:
        K -= 1

plus.sort()
minus.sort()


ans = 10000000000

for i in range(len(plus)):
    if 0 <= K-i < len(minus):
        ans = min(ans,plus[i]*2 +minus[K-i])
for i in range(len(minus)):
    if 0 <= K-i < len(plus):
        ans = min(ans,minus[i]*2 +plus[K-i])
print(ans)
