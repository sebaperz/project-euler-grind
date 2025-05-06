# 19. Counting Sundays
# https://projecteuler.net/problem=19


week = [0, 1, 2, 3, 4, 5, 6]

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def first_of_month(last_month, last_month_first_day):
    last_month_days = month[last_month]
    return (last_month_first_day + last_month_days) % 7


day = 0
count_of_sundays = 0

for i in range(1, 12):
    day = first_of_month(i, day)

for year in range(1901, 2001):
    if leap_year(year):
        month[1] = 29
    else:
        month[1] = 28

    for j in range(0, 12):
        day = first_of_month(j, day)
        if day == 6:
            count_of_sundays += 1

print(count_of_sundays)
