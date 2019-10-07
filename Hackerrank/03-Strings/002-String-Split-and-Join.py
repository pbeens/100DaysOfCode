# 002-String-Split-and-Join.py
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# this is a string  >>> this-is-a-string


def split_and_join(line):
    new_line = '-'.join(line.split())
    return new_line


line = input()
result = split_and_join(line)
print(result)
