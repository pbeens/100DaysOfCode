# 009-Designer-Door-Mat.py
# https://www.hackerrank.com/challenges/designer-door-mat/problem

# Note: consider the use of str.center(width[, fillchar])

debug = False

if debug:
    n, m = 7, 21
else:
    ip = input().split()
    n, m = int(ip[0]), int(ip[1])

# top half
for i in range(n // 2):
    str = ''
    for j in range(i):
        str += '.|.'
    str += '.|.'
    for j in range(i):
        str += '.|.'
    print(str.center(m, '-'))

# middle line
print('WELCOME'.center(m, '-'))


# botton half
for i in range(n // 2 - 1, -1, -1):
    str = ''
    for j in range(i):
        str += '.|.'
    str += '.|.'
    for j in range(i):
        str += '.|.'
    print(str.center(m, '-'))
