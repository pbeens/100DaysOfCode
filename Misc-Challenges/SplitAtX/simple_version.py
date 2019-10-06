# From https://twitter.com/BeingDanNolan/status/1179837518193266693
# Req'ts: https://github.com/pbeens/100DaysOfCode/blob/master/Misc-Challenges/SplitAtX/2019-10-06-12-38-42.png
# This is a simplified version using no parameters and fixed (not random) x and s.


def split_at_x():
    # do the split
    index_of_char = s.find(x)
    split_1 = s[:index_of_char]
    split_2 = s[index_of_char + 1:]

    # return the string with the max length
    if len(split_1) > len(split_2):
        return(split_1)
    elif len(split_2) > len(split_1):
        return(split_2)
    else:
        return('Same length!')


s = '_,rCqe):"Wrq,O"k$h<Cd'
x = 'C'

print(split_at_x())
