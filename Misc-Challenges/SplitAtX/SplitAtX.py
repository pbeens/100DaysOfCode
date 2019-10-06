# From https://twitter.com/BeingDanNolan/status/1179837518193266693
# Req'ts: https://github.com/pbeens/100DaysOfCode/blob/master/Misc-Challenges/SplitAtX/2019-10-06-12-38-42.png


import random
import string

# warm fuzzy feeling
debug = False


def split_at_x(x, s):
    # do the split
    index_of_char = s.find(x)
    split_1 = s[:index_of_char]
    split_2 = s[index_of_char + 1:]
    if debug:
        return(split_1, split_2)

    # return the string with the max length
    if len(split_1) > len(split_2):
        return(split_1)
    elif len(split_2) > len(split_1):
        return(split_2)
    else:
        return('Same length!')


# create a random string
str_len = 20
s = ''.join(random.choice(string.ascii_letters + string.punctuation)
            for i in range(str_len+1))
if debug:
    print(f'The string is: {s}')

# what do I want to split at
# make sure it's not the beginning or end!
char_to_split_at = random.choice(s[1:-1])
if debug:
    print(f'Splitting at {char_to_split_at}')

print(split_at_x(char_to_split_at, s))
