# 006-String-Validators.py
# https://www.hackerrank.com/challenges/string-validators/problem

# imports
import string

# set up variables
alphanum, alphabet, digit, lower, upper = False, False, False, False, False

# make it easier to test!
debug = True

# input
if debug:
    s = 'qA2'
else:
    s = input()

# process
for c in s:
    if c.isalnum():
        alphanum = True
    if c.isalpha():
        alphabet = True
    if c.isdigit():
        digit = True
    if c.islower():
        lower = True
    if c.isupper():
        upper = True

# output
print(f'{alphanum}\n{alphabet}\n{digit}\n{lower}\n{upper}')
