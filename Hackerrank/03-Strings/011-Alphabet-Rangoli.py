# 011-Alphabet-Rangoli.py
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


debug = True


def print_rangoli(size):
    # top half
    for i in range(size, 0, -1):
        print(i)
    # middle line
    print('middle line')
    # bottom half
    for i in range(1, size+1):
        print(i)


# input
if debug:
    n = 5
else:
    n = int(input())

print_rangoli(n)
