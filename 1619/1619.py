N,Z,W = [int(i) for i in input().split()]
a_max = 0
a_last = -1
for i in range(N):
    a = int(input())
    if a_max < a:
        a_max = a
    if i == N-1:
        a_last = a
ans = a_last - 
