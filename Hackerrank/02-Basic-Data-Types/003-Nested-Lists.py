# 003-Nested-Lists.py
# https://www.hackerrank.com/challenges/nested-list/problem

test_case = '''5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''

# warm fuzzy feeling
debug = False

# init vars
lst = []
scores = []

# read n
n = int(input())

# read and process names and scores
for i in range(n):
    name = input()
    score = float(input())
    lst.append([name, score])
    scores.append(score)

# find lowest score and remove from list of scores
min_score = min(scores)
other_scores = [score for score in scores if score != min_score]

# the 2nd lowest is...
second_min_score = min(other_scores)

#  need indexes of these scores
indexes_of_second_min_score = [i for i in range(
    len(scores)) if scores[i] == second_min_score]

# warm fuzzy feeling
if debug:
    print(f'indexes_of_second_min_score: {indexes_of_second_min_score}')

# print the names that correspond to the indexes
names = []
for i in indexes_of_second_min_score:
    names.append(lst[i][0])
for name in sorted(names):  # must be alpha
    print(name)
