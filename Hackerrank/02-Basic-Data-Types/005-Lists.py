# 005-Lists.py
# https://www.hackerrank.com/challenges/python-lists/problem

# I had to be careful about this because '10' comes before '2' when sorted, meaning I had to convert all the numbers to integers before adding to the list.

sample_data = '''12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''

# initialize our list
lst = []

# read in number of lines
n = int(input('n:'))

# read all lines into a list
commands = []
for i in range(n):
    commands.append(input())

# process the commands!
# See https://www.hackerrank.com/challenges/python-lists/tutorial for things you can do with a list
for command in commands:
    command_split = command.split()
    verb = command_split[0]
    if verb == 'insert':
        loc = int(command_split[1])
        num = int(command_split[2])
        lst.insert(loc, num)
    elif verb == 'print':
        print(lst)
    elif verb == 'remove':
        num = int(command_split[1])
        lst.remove(num)
    elif verb == 'append':
        num = int(command_split[1])
        lst.append(num)
    elif verb == 'sort':
        lst.sort()
    elif verb == 'pop':
        lst.pop()
    elif verb == 'reverse':
        lst.reverse()
    else:
        print('INVALID ENTRY')
