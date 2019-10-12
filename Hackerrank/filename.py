# This utility lets me enter the exercise number and name and it will create the file. Yes, I'm lazy...

import os
from pathlib import Path
import string

# update these variables with the challenge info
folder = '03-Strings'
url = 'https://www.hackerrank.com/challenges/merge-the-tools/problem'
n = '014'
s = 'Merge the Tools'

# quietly create the directory if it doesn't exist
# (from https://realpython.com/working-with-files-in-python/creating-a-single-directory)
p = Path(folder)
p.mkdir(exist_ok=True)

# create the file in the folder
s_new = s.replace(' ', '-')  # no spaces in filename!
filename = f'{n}-{s_new}.py'
here = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(here, folder, filename)
print(filepath)
try:
    f = open(filepath, 'w')
    f.write(f'# {filename}\n')
    f.write(f'# {url}\n\n')
    f.close()
except IOError:
    print('Wrong path provided')
print(f'{folder}\{n}-{s_new}.py created!')
