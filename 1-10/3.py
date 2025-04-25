#3. Largest Prime Factor
#https://projecteuler.net/problem=3

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        print(f"antes= i: {i}  n: {n}")
        if n % i:
            i += 1
        else:
            n //= i
        print(f"despues= i: {i}  n: {n}")
    return n
print(largest_prime_factor(600851475143))
