# 12. Highly divisible triangular number
# https://projecteuler.net/problem=12

output = 100000
divisor = 0
contador = output
while divisor < 250:
    output += contador
    contador += 1
    divisor = 0
    for i in range(1, int(output**0.5)):
        if output % i == 0:
            divisor += 1

print(output, divisor)
