# 08-Set-.symmetric_difference()-Operation.py
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

sample_input = '''9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
'''  # should return 8

# input
n1 = int(input())
students1 = set(input().split())
n2 = int(input())
students2 = set(input().split())

# process and output
print(len(students1 ^ students2))  # aka symmetric_difference()
