# 12. Highly divisible triangular number
# https://projecteuler.net/problem=12
# what is the value of the first triangle number to have over 500 divisors
#

import numpy as np

def npDivs(N):
    divs = np.arange(1,int(N**0.5)+1)  # potential divisors up to √N
    divs = divs[N % divs==0]           # divisors
    comp = N//divs[::-1]               # complement quotients
    return np.concatenate((divs,comp[divs[-1]==comp[0]:])) # combined
for i in range(100,1000000):
    print(npDivs(i))
