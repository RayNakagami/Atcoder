a  = input()
 
ans = 0
a = [int(i) for i in input().split()]
 
for num in a:
  ans += num - 1
  
print(ans)
