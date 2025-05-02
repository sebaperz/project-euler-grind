# 12. Highly divisible triangular number
# https://projecteuler.net/problem=12

#output = 100000
#divisor = 0
#contador = output
#while divisor < 20:
#    output += contador
#    contador += 1
#    divisor = 0
#    for i in range(1, int(output**0.5)):
#        if output % i == 0:
#            divisor += 1

#print(output, divisor)

def triangular_number(n):
    output = 1
    for i in range(n):
        output += 1
        output *= (i + 1)
    return output

def divisors(n):
    divisor = 0
    for i in range(1, int(n**0.5)):
        if n % i == 0:
            divisor += 1
    return divisor

def prime_factors(n):
    output = []
    for i in range(2, n + 1):
        if n % i == 0:
            output.append(i)
    return output

import math

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            sieve[num*num : limit+1 : num] = [False] * len(sieve[num*num : limit+1 : num])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def count_divisors(n, primes):
    if n == 1:
        return 1
    count = 1
    for p in primes:
        if p * p > n:
            break
        exponent = 0
        while n % p == 0:
            exponent += 1
            n = n // p
        count *= (exponent + 1)
    if n > 1:
        count *= 2
    return count

def find_triangle_number_with_over_k_divisors(k):
    primes = sieve_of_eratosthenes(10**6)  # Adjust the limit based on expected n
    n = 1
    while True:
        triangle = n * (n + 1) // 2
        if n % 2 == 0:
            a = n // 2
            b = n + 1
        else:
            a = n
            b = (n + 1) // 2
        num_divisors = count_divisors(a, primes) * count_divisors(b, primes)
        if num_divisors > k:
            return triangle
        n += 1

k = 500
result = find_triangle_number_with_over_k_divisors(k)
print(result)
