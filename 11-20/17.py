# 17. Number Letter Counts
# https://projecteuler.net/problem=17

print(len("threehundredandforty-two"))


def count_letters(num):

    total = ""

    unit = ["", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]
    dec = ["", "teen", "twenty", "thirty", "forty",
           "fifty", "sixty", "seventy", "eighty", "ninety"]
    cen = ["hundred"]
    mil = ["thousand"]
    mill = ["million"]

    if num == 11:
        return len("eleven")
    elif num == 12:
        return len("twelve")


trece13 = "thirteen"
