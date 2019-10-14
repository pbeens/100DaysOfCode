# 01-Set.add().py
# https://www.hackerrank.com/challenges/py-set-add/problem

sample = '''7
UK
China
USA
France
New Zealand
UK
France 
'''  # should print 5

countries = set()  # new blank set

# input
num = int(input())  # how many?
for n in range(num):  # input that many times
    countries.add(input().strip())  # add each country

# output
print(len(countries))
