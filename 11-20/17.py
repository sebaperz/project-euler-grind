# 17. Number Letter Counts
# https://projecteuler.net/problem=17


def count_letters(num):
    total = ""
    if num == 1000:
        return len("onethousand")
    antil20 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
               "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    decena = ["", "", "twenty", "thirty", "forty",
              "fifty", "sixty", "seventy", "eighty", "ninety"]

    # first 2 digits
    two_digits = num % 100
    if two_digits < 20:
        total += antil20[two_digits]
    else:
        total += decena[two_digits // 10] + antil20[two_digits % 10]

    # hundreds
    hundreds = num // 100
    if hundreds > 0:
        total += antil20[hundreds] + "hundred"
        if two_digits > 0:
            total += "and"

    return len(total)


print(sum(count_letters(i) for i in range(1, 1001)))
