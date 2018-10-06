n = int(input())

a = [int(i) for i in input().split()]
ans = []
for i in range(1,n):
    if a[i] == 1:
        ans.append(a[i-1])
ans.append(a[n-1])
print(len(ans))
for i in ans:
    print(i,end = ' ')
print()
