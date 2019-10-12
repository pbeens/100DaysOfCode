# 011-Alphabet-Rangoli.py
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# solution from https://www.hackerrank.com/challenges/alphabet-rangoli/editorial

debug = False

# input
if debug:
    n = 5
else:
    n = int(input())

# output
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))
