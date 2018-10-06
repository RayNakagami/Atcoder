n = int(input())

flag = True
chr = 'A'
table = []
for i in range(n):
    line = input()
    if not(chr == line[0] or chr == 'A'):
        print('No')
        flag = False
        break

    if line in table:
        print('No')
        flag = False
        break
    table.append(line)
    chr = line[-1]

if flag:
    print('Yes')
