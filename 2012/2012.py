def cube(x):
    i = 1
    while(True):
        if i**3 > x:
            return i-1
        else:
            i += 1

while(True):
    
    e = int(input())
    if e==0:
        break
    ans = pow(10,16)
    z_max = cube(e)
    for z in range(z_max+1):
        y = int(pow(e-z**3,1/2))
                                
        ans = min(ans,e-y*y+y-z*z*z+z)
    print(ans)
