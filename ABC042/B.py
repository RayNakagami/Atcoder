l = input().split(' ')

N = int(l[0])
L = int(l[1])
S=[]
for i in range(N):
    S.append(input())

S.sort()

for str in S:
    print(str,end="")

print()
