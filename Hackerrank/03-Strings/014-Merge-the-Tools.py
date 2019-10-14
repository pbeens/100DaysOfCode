# 014-Merge-the-Tools.py
# https://www.hackerrank.com/challenges/merge-the-tools/problem

debug = True


def merge_the_tools(string, k):
    """Prints the characters in k groups, not printing any characters already in the group

    Arguments:
        string {string} -- string to be printed
        k {int} -- number of groups
    """
    s_tmp = ''
    for i in range(len(string)):
        # print after every group
        if i % k == 0 and i != 0:
            print(s_tmp)
            s_tmp = ''
        # check if letter is already added
        if string[i] not in s_tmp:
            s_tmp += string[i]
    print(s_tmp)  # last one


# input
if debug:
    string, k = 'AABCAAADA', 3
else:
    string, k = input(), int(input())

# run the function
merge_the_tools(string, k)
