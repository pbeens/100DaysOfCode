# 01-Introduction-to-Sets.py
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

sample_data = '''10
161 182 161 154 176 170 167 171 170 174
'''

# initialize set
heights_set = set()


def average(array):
    """Returns average of the unique values in arracy

    Arguments:
        array {list of ints} -- an array of plant heights
    """
    # convert to set
    heights_set = set(array)
    # calc avg and output
    return(sum(heights_set)/len(heights_set))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
