H ,W = [int(i) for i in input().split(' ')]
s = []
#print(s)
for i in range(H):
    line = input()
    lis = []
    for str in line:
        lis.append(str)
    s.append(lis)


def drawable(h,w):
    for i in [-1,1]:
        if 0 <= w+i < W:
#            print(h,w+i)
            if s[h][w+i] =='#':
                return True
    for i in [-1,1]:
        if 0 <= h+i < H:
            if s[h+i][w] =='#':
                return True

    return False

flag = True
for i in range(H):
    for j in range(W):
#        print(i,j)
        if s[i][j]=='#' and not(drawable(i,j)):
           flag = False 

if flag:
    print("Yes")
else:
    print("No")
