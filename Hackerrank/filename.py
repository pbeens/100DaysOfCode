# This utility lets me enter the exercise number and name and it will create the file. Yes, I'm lazy...

import os
from pathlib import Path
import string


# update these variables with the challenge info
folder = '04-Sets'
url = 'https://www.hackerrank.com/challenges/py-set-intersection-operation/problem'
n = '06'
s = 'Set .intersection() Operation'


# quietly create the directory if it doesn't exist
# (from https://realpython.com/working-with-files-in-python/creating-a-single-directory)
p = Path(folder)
p.mkdir(exist_ok=True)

# assemble filename
s_new = s.replace(' ', '-')  # no spaces in filename!
filename = f'{n}-{s_new}.py'  # like this: 014-Merge-the-Tools.py

# make sure!!!
prompt = input(
    f'Are you sure? This will overwrite {folder}\{filename}. (Y/N): ')
if prompt.upper() != 'Y':
    print('File not created!')
    exit()

# create the file in the folder
here = os.path.dirname(os.path.realpath(__file__))  # assemble the path
filepath = os.path.join(here, folder, filename)
print(filepath)  # not needed, but is reassuring
try:  # create the file and put in the header
    f = open(filepath, 'w')
    f.write(f'# {filename}\n')
    f.write(f'# {url}\n\n')
    f.close()
    print(f'{folder}\{filename} created!')
except IOError:
    print('Wrong path provided')
