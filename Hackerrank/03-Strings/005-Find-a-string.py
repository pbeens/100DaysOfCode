# 005-Find-a-string.py
# https://www.hackerrank.com/challenges/find-a-string/problem

sample_input = '''ABCDCDC
CDC
'''  # --> 2


def count_substring(string, sub_string):
    """Searches for the number of occurrences of a substring in a string

    Arguments:
        string {string} -- the string to be searched
        sub_string {string} -- the substring to search for

    Returns:
        int -- the number of occurrences of the substring in the string
    """

    counter = 0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            counter += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
