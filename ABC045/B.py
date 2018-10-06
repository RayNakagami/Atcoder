A = input()
B = input()
C = input()

next_p = 'a'
while True:
    if next_p == 'a':
        if A == '':
            print("A")
            break
        next_p = A[0]
        A = A[1:]
#        print(next_p,A)

    if next_p == 'b':
        if B == "":
            print("B")
            break
        next_p = B[0]
        B = B[1:]
#        print(next_p,B)

    if next_p == 'c':
        if C == "":
            print("C")
            break
        next_p = C[0]
        C = C[1:]
#        print(next_p,C)


