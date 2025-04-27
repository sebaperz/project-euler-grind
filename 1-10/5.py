# 5. Smallest multiple
# https://projecteuler.net/problem=5

def smallest_multiple(num):
    factorial = 1
    for i in range(1,num+1):
        factorial *= i

    for i in range(num, factorial, num):
        #all(a_list): return True if all elements of a_list are True
        if all(i % j == 0 for j in range( 1, num+1)):
            return i

print(smallest_multiple(20))
