H , W = [int(i) for i in input().split()]

a = []

for i in range(H):
    line = [int(i) for i in input().split()]
    a.append(line)
ans = []
for i in range(H):
    for j in range(W-1):
        if a[i][j] % 2 == 1:
            ans.append(str(i+1) + ' '+ str(j+1)+' '+str(i+1) + ' '+str(j+2))
            a[i][j+1] += 1


for i in range(H-1):
    if a[i][W-1] % 2 ==1:
        ans.append(str(i+1)+' '+str(W)+' '+str(i+2)+' '+str(W))
        a[i+1][W-1] +=1
print(len(ans))
for i in ans:
    print(i)
