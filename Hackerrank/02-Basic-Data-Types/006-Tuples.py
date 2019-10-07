# 006-Tuples.py
# https://www.hackerrank.com/challenges/python-tuples/problem

sample_data = '''2
1 2
'''
# should output 3713081631934410656

n = int(input())
integer_list = map(int, input().split())

print(hash(tuple(integer_list)))

# Note: This is giving me a different value at home (1299869600) than at Hackerrank (3713081631934410656). I don't know why.
