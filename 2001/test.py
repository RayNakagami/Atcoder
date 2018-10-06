#print(not(isinstance(print(),type(None))))
primes = []
for i in range(2,int(input())):
    for prime in primes:
        if i % prime ==0 or i < prime*prime:
            break
        primes.append(i)


print(primes)
