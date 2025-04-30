# 12. Highly divisible triangular number
# https://projecteuler.net/problem=12
# what is the value of the first triangle number to have over 500 divisors
#

output = 0
while True:
    output += 1
    contador = output
    divisor = 0
    while contador > 0:
        if output % contador == 0:
            divisor += 1
        contador -= 1
    if divisor > 500:
        break
print(output)
