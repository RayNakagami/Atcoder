s = input()
t = input()

i = 0
while i < len(s) and i <len(t) and s[i] == t[i]:
    i+=1

maxLen = i

i = 0
while i < len(s) and i < len(t) and s[-i-1] == t[-i-1]:
    i +=1

maxLen = max(i,maxLen)

print(len(s) + len(t) - 2*maxLen)

