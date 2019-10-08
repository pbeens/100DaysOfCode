# 003-Whats-Your-Name
# https://www.hackerrank.com/challenges/whats-your-name/problem
#
# Note: f-strings makes this kind of task so much easier to do! It is worth
# taking the time to learn how to use them.

sample_input = '''Ross
Taylor
'''


def print_full_name(a, b):
    print(f'Hello {a} {b}! You just delved into python.')


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
