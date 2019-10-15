# 03-Symmetric-Difference.py
# https://www.hackerrank.com/challenges/symmetric-difference/problem

'''
Sample Input
4
2 4 5 9
4
2 4 11 12

Sample Output
5
9
11
12
'''

m = int(input())
m_int_set = set(map(int, input().split()))
n = int(input())
n_int_set = set(map(int, input().split()))

union = m_int_set.union(n_int_set)
intersection = m_int_set.intersection(n_int_set)
sim_diff_set = union.difference(intersection)
print(sim_diff_set)

# Method 1
# for n in sorted(sim_diff_set):
#     print(n)

# Method 2 - Comprehension
print('\n'.join(str(item) for item in sorted(sim_diff_set)))
