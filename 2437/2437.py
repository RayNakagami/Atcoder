table= {}
def solve(dict,key):
    global table
    if key in table:
    #    print('key=',key)
        return table[key]
    ret = []
    #print(key)
    for i in dict[key]:
        if i[0] == '[':
            ret.append(i[1:-1])
        else:
            ret += (solve(dict, i))
    if len(ret) > 200:
        for i in table.keys():
            table[i]=''
            return ''
    table[key] = ret
    #print(key)
    return ret

Na, Nt, Ng, Nc = [int(i) for i in input().split()]
m = int(input())

dict = {}

for i in range(m):
    key, value = [i for i in input().split(': ')]
    if i == 0:
        aa = key
    value = value.split()
    dict[key] = value

lis = solve(dict, aa)
if len(lis)==Na+Nt+Ng+Nc:
    DP = [[[[0 for i in range(Nc+1)]for j in range(Ng+1)]for k in range(N+1)]for l in range(len(lis)+1)]
    #print(DP[4])
    DP[0][0][0][0] = 1 
    #print(DP)
    for i in range(len(lis)):
        str = lis[i]
        for a in range(i+1):
            if a > Na:
                break
            for t in range(i-a+1):
                if t > Nt:
                    break
                for g in range(i-a-t+1):
                    if g > Ng:
                        break
#                    print(i,a,t,g)
                    if i-a-t-g > Nc:
                        continue
                    ans = DP[a][t][g][c] % 1000000007
 #                   print(ans)
                    for char in str:
#                        print(i,a,t,g)
                        if char == 'A':
                            if a+1 > Na:
                                continue
                            DP[a+1][t][g][c] += ans
                        elif char == 'T':
                            if t+1 > Nt:
                                continue
                            DP[a][t+1][g][c] += ans
                        elif char == 'G':
                            if g+1 > Ng:
                                continue
                            DP[a][t][g+1][c] += ans
                        elif char == 'C':
                            if i-a-t-g+1> Nc:
                                continue
                            DP[a][t][g][c+1] += ans
#                        print(DP)
                    #DP[i][a][t][g] = ans % 1000000007

    print(DP[len(lis)][Na][Nt][Ng]%1000000007)
else:
    print(0)
