l = input().split(' ')

y = int(l[3]) - int(l[1])
x = int(l[2]) - int(l[0])

def my_print(i,str):
    for j in range(i):
        print(str,end='')
"""
for i in range(x):
    print('U',end='')

for i in range(y):
    print('R',end='')

for i in range(x):
    print('D',end='')

for i in range(y+1):
    print('L',end='')

for i in range"
"""
my_print(y,'U')
my_print(x,'R')
my_print(y,'D')
my_print(x+1,'L')
my_print(y+1,'U')
my_print(x+1,'R')
my_print(1,'D')
my_print(1,'R')
my_print(y+1,'D')
my_print(x+1,'L')
my_print(1,'U')


print()
