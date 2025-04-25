#2. Even Fibonacci Numbers
#https://projecteuler.net/problem=2

fib = [1, 2]
sum_of_even = 2
while fib[-1]<4000000:
    num = fib[-1]+fib[-2]
    if num % 2 == 0:
        sum_of_even += num
    fib.append(num)
print(sum_of_even)
