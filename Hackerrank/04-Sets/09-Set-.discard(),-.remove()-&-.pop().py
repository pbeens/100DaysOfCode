# 09-Set-.discard(),-.remove()-&-.pop().py
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

# Note:could be done more efficiently with eval()

sample_input = '''9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
'''  # should return 4

# input
num_data_items = int(input())
data = set(map(int, input().split()))
num_commands = int(input())
commands = []
for s in range(num_commands):
    commands.append(input())

# process
for command in commands:
    cmd = command.split()  # examples: discard 5, pop
    if cmd[0] == 'pop':
        data.pop()
    elif cmd[0] == 'discard':
        data.discard(int(cmd[1]))
    elif cmd[0] == 'remove':
        data.remove(int(cmd[1]))

# output
print(sum(data))
