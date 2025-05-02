# 16. Power digit sum
# https://projecteuler.net/problem=16

def power_digit_sum(num):
    return sum([int(x) for x in str(num)])

print(power_digit_sum(2**1000))
