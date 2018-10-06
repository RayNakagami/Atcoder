line = input()
flag = True

for i in range(int(input())):
  if not(line[i]== '1'):
    print(line[i])
    flag = False
    break

if flag:
  print('1')
