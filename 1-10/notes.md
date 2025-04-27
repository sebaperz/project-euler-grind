# Notes for the code of the exercises of project euler

## About Primes:
```python
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```
It checks if **n** have any divisors, (if it does not, then **n** is prime) if **i** is a divisor:
change our **n** to "**n** // **i**", and continues checking for the divisors of **n**.
If it does not find any, then **n** is prime.

## all()
**all(iterable)** returns True if all elements in the iterable are true.
```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```
