N = int(input())

paper = {}
for i in range(N):
    t = int(input())
#    print(t)
 #   print(paper)
    if t in paper:
        paper[t] = not(paper[t])
    else:
        paper[t] = True

ans = 0
for b in paper.values():
    if b:
        ans +=1

print(ans)
#print(paper)
