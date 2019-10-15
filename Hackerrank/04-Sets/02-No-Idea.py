# 01-No-Idea.py
# https://www.hackerrank.com/challenges/no-idea/problem

import time

debug = True

sample_data = '''3 2
1 5 3
3 1
5 7
'''

if debug:
    n = 3
    m = 2
    array = '1 5 3'.split()
    likes = '3 1'.split()
    dislikes = '5 7'.split()
else:
    n, m = input().split()  # don't need to use!
    array = input().split()
    likes = set(input().split())
    dislikes = set(input().split())

# print('Method 1')
# start_time = time.time()
# for i in range(100000):
#     score = sum((n in likes) - (n in dislikes) for n in array)
# print(score)
# print("--- %s seconds ---" % (time.time() - start_time))

print('Method 2')
start_time = time.time()
for i in range(100000):
    score = 0
    for n in array:
        if n in likes:
            score += 1
        if n in dislikes:
            score -= 1
print(score)
print("--- %s seconds ---" % (time.time() - start_time))
