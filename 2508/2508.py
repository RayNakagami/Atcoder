def reset(n_lis,chr_lis):
    k = len(n_lis)
    for i in range(len(chr_lis)):
        n = ord(chr_lis[i])
        a = n_lis[i%k]
        """
 #       print(n_lis)
       # if  n>96 and n-a<97:
            n -= 6
        if n-a<65:
            n+=58
        n-=a
        chr_lis[i]=chr(n)
"""
        c_type = True
        n -= 64
        if n > 27:
            n -=32
            c_type = False
        n -= a
        if n<1:
            n+=26
            c_type=not(c_type)
        if n<1:
            n+=26
            c_type=not(c_type)
        
        if c_type:
            n+=64
        else:
            n+=96
        
        chr_lis[i]=chr(n)


    for ch in chr_lis:
        print(ch,end='')
    print()

while True:
    if input()=='0':
        break
    n_lis = [int(i) for i in input().split(' ')]
    c_lis = [i for i in input()]
    reset(n_lis,c_lis)
