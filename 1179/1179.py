n = int(input())

def solve(Y,M,D):
    ans = 0
    ans += (Y - 1) * (19 + 20) * 5
    ans += ((Y -1)// 3) * 5
    ans += 19 * (M-1)
    if Y % 3 ==0:
        ans += (M-1)
    else:
        ans += (M // 2)
    ans += (D-1)
    print(196470 - ans)
    

for i in range(n):
    l = input().split(' ')
  
    solve(int(l[0]) , int(l[1]), int(l[2]))

