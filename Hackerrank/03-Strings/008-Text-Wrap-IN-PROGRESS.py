# 008-Text-Wrap.py
# https://www.hackerrank.com/challenges/text-wrap/problem

sample_input = '''ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
'''


import textwrap

def wrap(string, max_width):
    s = "\n".join(textwrap.wrap(string, max_width))
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)y