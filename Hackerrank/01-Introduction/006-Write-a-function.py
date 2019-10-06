case_1 = [1800, 1900, 2100, 2200, 2300 and 2500]  # False
case_2 = [2000, 2400]  # True
case_3 = [1923, 2001, 1875]  # False


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


for year in case_3:
    print(is_leap(year))
