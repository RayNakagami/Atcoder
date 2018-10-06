def check(str1,str2):
    if not(len(str1)==len(str2)):
        return False
    for i in range(len(str1)):
        if not(str1[i]==str2[i]):
            return False

    return True

def solve(a,b):
    if not(len(a)==len(b)):
        print("DIFFERENT")
        return
    flag = True
    for i in range(len(a)):
        if not(check(a[i],b[i])):
            if i%2 ==1:
                if not(flag):
                    print("DIFFERENT")
                    return
                if flag:
                    flag = False
            else:
                print("DIFFENRENT")
                return

    if flag:
        print("IDENTICAL")
    else:
        print("CLOSE")
                    
while True:    
    a=input().split('"')
    if a[0]=='.':
        break
    b=input().split('"')
    solve(a,b)
