# 10. Summation of primes
# https://projecteuler.net/problem=10

def is_prime(num):
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

primes = [2]
for i in range(3, 2000000, 2):
    if is_prime(i):
        primes.append(i)

print(sum(primes))
