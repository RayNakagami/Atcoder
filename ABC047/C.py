str = input()
flag = str[0]
count=0
for i in str:
    if not(flag==i):
        flag=i
        count +=1

print(count)
