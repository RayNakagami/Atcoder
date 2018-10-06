lC = ['a','b','c','d','e','f','g','h','i','j','k','l','m',',n','o','p','q','r','s','t',
'u','v','w,','x','y','z']

def solve(S):
    if not(S[0] == 'A'):
        return "WA"
    if S[-1] == 'C':
        return "WA"
    if not(S[1] in lC):
        return "WA"
    
    flag = False
    for i in range(1,len(S)):
        if S[i] == 'C':
            if flag:
                return "WA"
            flag = True
            continue
        if not(S[i] in lC):
            return "WA"
    if not(flag):
        return "WA"
    return "AC"
    

S = input()
print(solve(S))
