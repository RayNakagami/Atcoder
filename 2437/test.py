table= {}
def solve(dict,key):
    global table
    if key in table:
        return table[key]
    ret = []
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
    current =0
    next = 1
    DP = [[[[0 for i in range(2)] for j in range(Ng+1)]for k in range(Nt+1)]for l in range(Na+1)]
    DP[0][0][0][0] = 1
    for i in range(len(lis)):
        hA=hT=hG=hC=False
        #print(i)
        for char in lis[i]:
            if char == 'A':
                hA = True
            elif char == 'G':
                hG  = True
            elif char == 'T':
                hT = True
            else:
                hC = True
        for a in range(i+1):
            if a > Na:
                break
            for t in range(i-a+1):
                if t > Nt:
                    break
                for g in range(i-a-t+1):
                    if g > Ng:
                        break
                    c = i-a-t-g
                    if c > Nc:
                        continue
                    ans = DP[a][t][g][current] % 1000000007
                    if hA and a+1 <= Na:
                        DP[a+1][t][g][next] += ans
                    if hT and t+1 <= Nt:
                        DP[a][t+1][g][next] += ans
                    if hG and g+1 <=  Ng:
                        DP[a][t][g+1][next] += ans
                    if hC and c+1 <= Nc:
                        DP[a][t][g][next] += ans
        #DPC = DPN
        N=current
        current = next
        next = N
        for i in range(Na+1):
            for j in range(Nt+1):
                for k in range(Ng+1):
                    DP[i][j][k][next] = 0
    print(DP[Na][Nt][Ng][current]%1000000007)
else:
    print(0)
