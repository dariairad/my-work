# Lecture 5.2 List Example - Primes

# Program generating prime numbers

primes = []
upTo = 1001

for candidate in range(2, upTo):
    # print (candidate)
    isPrime = True
    for divisor in primes:
    # rather than in range (2, candidate) for efficiancy. Only need to check if divisable by prime
        # if divisable by an int it is not a prime number
        if (candidate % divisor == 0):
            isPrime = False
            # so there is no need for checking
            break
    if isPrime:
        primes.append(candidate)

print (primes)