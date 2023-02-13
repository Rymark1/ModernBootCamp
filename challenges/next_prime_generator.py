def next_prime():
    nbr = 2
    while True:
        if len([x for x in range(nbr) if nbr % (x+1) == 0]) == 2 or nbr == 2:
            yield nbr
        nbr += 1


primes = next_prime()
print([next(primes) for i in range(25)])
