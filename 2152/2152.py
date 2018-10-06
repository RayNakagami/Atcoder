bord = []

while True:
    n = int(input())
    c=0
    for i in range(n):
        lis = input().split(' ')
        if lis[0] =='W':
            s = int(lis[1])
            t = int(lis[2])

