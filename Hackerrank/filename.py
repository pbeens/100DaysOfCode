# This utility lets me enter the exercise number and name and it will produce a filename that I can use to create the file. Yes, I'm lazy...

import string

n = '013'
s = 'The-Minions-Game'

s_new = s.replace(' ', '-')  # no spaces in filename!
print(f'{n}-{s_new}.py')
