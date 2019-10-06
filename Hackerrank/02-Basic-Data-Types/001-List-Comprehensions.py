# 001-List-Comprehensions.py
# https://www.hackerrank.com/challenges/list-comprehensions/problem

x, y, z, n = 1, 1, 1, 2

lst = [[i, j, k] for i in range(x + 1) for j in range(y + 1)
       for k in range(z + 1) if ((i + j + k) != n)]
print(lst)
