def check(num1,num2):
    return format(num1^num2,'b').count('1')

c = 0
for i in range(31):
    if check(i,0) <= 3 and check(i,3) <= 3:
        print(""+"0"*(5-len(format(i,'b')))+format(i,'b'))
        c += 1

print(c)
