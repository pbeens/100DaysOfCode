# 001-sWAP-cASE.py
# https://www.hackerrank.com/challenges/swap-case/problem

# test case
# HackerRank.com presents "Pythonist 2".
# becomes:
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

import string


def swap_case(s):
    s2 = ''
    for c in s:
        if c in string.ascii_uppercase:
            s2 += c.lower()
        elif c in string.ascii_lowercase:
            s2 += c.upper()
        else:
            s2 += c
    return s2


s = input()
result = swap_case(s)
print(result)
