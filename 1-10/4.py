# 4. Largest Palindrome Product
# https://projecteuler.net/problem=4

def is_palindrome(num):
    return str(num) == str(num)[::-1]

max_palindrome = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product

print(max_palindrome)
