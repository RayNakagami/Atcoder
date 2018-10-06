def check(str1,str2):
    if not(len(str1)==len(str2)):
        return False 
    for i in range(len(str1)):
        if not(str1[i]==str2[i]):
            return False
    return True


def solve(s1,s2):
    #print(len(s1),len(s2))
    if not(len(s1) == len(s2)):
        print("DIFFERENT")
        return
    flag = True
    for i in range(len(s1)):
        if not(check(s1[i],s2[i])):
            if i%2==1:
                if flag:
                    flag = False
                else:
                    print("DIFFERENT")
                    return
            else:
                print("DIFFERENT")
                return
    if flag:
        print("IDENTICAL")
    else:
        print("CLOSE")
        
    return


while True:
    s1=input().split('"')
    if s1[0] == '.':
        break
    s2 = input().split('"')
    solve(s1,s2)

