# 012-Capitalize.py
# https://www.hackerrank.com/challenges/capitalize/problem


# main function
def solve(s):
    """Returns the words in the string capitalized

    Arguments:
        s {string} -- The string the be capitalized

    Returns:
        string -- The capitalized string
    """
    return ' '.join(word.capitalize() for word in s.split(' '))


# input
s = input()

# call the function
print(solve(s))
