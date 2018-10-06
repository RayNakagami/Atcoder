N,M =[int(i) for i in input().split(' ')]
table = [0]*N

for i in range(M):
    a,b = [int(i) for i in input().split(' ')]
    if a==1:
        table[b-1] +=1
        if b==N:
            table[b-1] +=1
    if b==N:
        table[a-1]+=1
#    print(table)
flag = True
for i in table:
    if i==2:
        print("POSSIBLE")
        flag = False
        break

if flag:
    print("IMPOSSIBLE")

#print(table)
