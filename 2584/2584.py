def c_to_int(char):
    return ord(char)-65

def solve(s):
    count = 0
    table=[]
    for str in s:
        if str=='+':
            count +=1
        elif str =='-':
            count -=1
        elif str=='[':
            table.append(str)
        elif str==']':
            table.append(str)
        elif str=='?':
            table.append(str)
            count =0
        else:
            table.append((c_to_int(str) +count)%26)
            count = 0

    for i in range(len(table)):
        if table[i]=='?':
            table[i] = 0
#    print(table)
    return(table)

def rev(table):
    ret = "" 
    i =0
    while i <  len(table):
        if table[i] == '[':
            c  = 1
            i_=i+1
            while c>0:
                if table[i_] =='[':
                    c += 1
                if table[i_] ==']':
                    c -= 1
                i_ += 1
 #           print(reversed(table[i+1:i_-1]))
            ret += rev(table[i+1:i_-1])[::-1]
            i = i_-1
        elif table[i] ==']':
            pass
        else:
#            print(chr(table[i]+65))
            ret += chr(table[i]+65)
        i+=1

    return ret


while True:
    S = input()
    if S[0]=='.':
        break
    ans = rev(solve(S))
    print(ans)
