# 7. 10001st Prime
# https://projecteuler.net/problem=7

def prime_num(num):
    list_of_primes = [2]
    candidate = 3
    while len(list_of_primes) < num:
        if is_prime(candidate):
            list_of_primes.append(candidate)
        candidate += 2
    return list_of_primes[-1]

def is_prime(num):
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

print(prime_num(10001))
