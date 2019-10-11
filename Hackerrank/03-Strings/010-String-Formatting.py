# 010-String-Formatting.py
# https://www.hackerrank.com/challenges/python-string-formatting/problem

# The editorial part of the challenge mentions this print technique:
# "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width = width)
# My preference is to do it with f-strings instead


def print_formatted(number):
    """prints number in decimal, octal, hexadecimal, binary, with the length of the binary value of number used as the width

    Arguments:
        number {decimal} -- number to print to, and width
    """
    width = len('{0:b}'.format(number))
    for i in range(1, number+1):
        print(f'{i:>{width}} {i:>{width}o} {i:>{width}X} {i:>{width}b}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
