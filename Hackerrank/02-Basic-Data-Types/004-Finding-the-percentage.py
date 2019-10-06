# 004-Finding-the-percentage.py
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

sample_input = '''3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
'''
# These input statements are from the challenge site. Note the advanced technique being used for the inputs
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

# warm fuzzy feeling
debug = False

# what's the parsed input?
if debug:
    print(student_marks)
    print(student_marks[query_name])

# do the math
# Note: See https://www.geeksforgeeks.org/find-average-list-python/ for some other ways to get the average of a list
num_marks = len(student_marks[query_name])
sum_marks = sum(student_marks[query_name])
avg_mark = sum_marks / num_marks

# output
print(f'{avg_mark:.2f}')  # note use of f-string and decimal formatting
