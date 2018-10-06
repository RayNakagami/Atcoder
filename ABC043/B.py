S = input()

#print(S)
ans = []

for str in S:
    if str == '0':
        ans.append('0')
    elif str == '1':
        ans.append('1')
    else:
        if len(ans) > 0:
            ans.pop()
            

for a in ans:
    print(a,end ="")


print()
