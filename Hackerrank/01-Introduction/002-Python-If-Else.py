# test cases
# n = 3  # Weird
n = 24  # Not Weird


def weird(n):
    '''(int -> str)
    Precondition 0 < n > 100

    Return Weird or Not Weird dependent on conditions

    >>> weird(3)
    'Weird'
    >>> weird(24)
    'Not Weird'

    '''

    if n % 2 == 1:  # odd
        return('Weird')
    if n in range(2, 5):  # 2 to 5 (4 really)
        return('Not Weird')
    else:
        if n in range(6, 21):  # 6 to 20
            return('Weird')
    return('Not Weird')  # over 20


print(weird(n))

# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())
