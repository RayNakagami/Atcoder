w = input()
lis = {}

for i in w:
    if i in lis:
        lis[i] = not(lis[i])
    else:
        lis[i] = False

flag = True
for b in lis.values():
    if not(b):
        print("No")
        flag = False
        break

if(flag):
    print("Yes")
