def moji(x,ans):
    if ans == 0:
        return
    if x == 1:
        if(ans%5==1):
            str = '.'
        elif(ans%5==2):
            str =','
        elif(ans%5==3):
            str='!'
        elif ans%5==4:
            str='?'
        else:
            str = ' '
    if x == 2:
        if(ans%3==1):
            str = 'a'
        elif(ans%3==2):
            str = 'b'
        else:
            str = 'c'
    if x == 3:
        if(ans%3==1):
            str = 'd'
        elif(ans%3==2):
            str = 'e'
        else:
            str = 'f'
    if x == 4:
        if(ans%3==1):
            str = 'g'
        elif(ans%3==2):
            str = 'h'
        else:
            str = 'i'
    if x == 5:
        if(ans%3==1):
            str = 'j'
        elif(ans%3==2):
            str = 'k'
        else:
            str = 'l'
    if x == 6:
        if(ans%3==1):
            str = 'm'
        elif(ans%3==2):
            str = 'n'
        else:
            str = 'o'
    if x == 7:
        if(ans%4==1):
            str = 'p'
        elif(ans%4==2):
            str = 'q'
        elif(ans%4==3):
            str ='r'
        else:
            str = 's'
    if x == 8:
        if(ans%3==1):
            str = 't'
        elif(ans%3==2):
            str = 'u'
        else:
            str = 'v'
    if x == 9:
        if(ans%4==1):
            str = 'w'
        elif(ans%4==2):
            str = 'x'
        elif ans%4==3:
            str = 'y'
        else:
            str = 'z'
    print(str,end="")
def solve(str):
    x = '-1'
    ans =0
    for s in str:
        if s == '0':
            moji(int(x),ans)
            ans = 0
        else:
            x = s
            ans +=1

N = int(input())
for i in range(N):
    solve(input())
    print()
