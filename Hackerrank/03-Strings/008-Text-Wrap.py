# 008-Text-Wrap.py
# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap
sample_input = '''ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
'''


def wrap(string, max_width):
    s = "\n".join(textwrap.wrap(string, max_width))
    return s


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
