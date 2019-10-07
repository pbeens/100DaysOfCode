# this set returns true
# m1 = [[1, -2], [-3, 4], [1, -2], [-3, 4]]
# m2 = [[2, -1], [0, -1], [2, -1], [0, -1]]

# this set returns false (differing length sub-lists)
# m1 = [[1, -2], [-3, 4], [1, -2], [-3, 4, 4]]
# m2 = [[2, -1], [0, -1], [2, -1], [0, -1]]

# this set returns false (differing length lists)
m1 = [[1, -2], [-3, 4], [1, -2], [-3, 4], [2, 4]]
m2 = [[2, -1], [0, -1], [2, -1], [0, -1]]


def lengths_equal(m1, m2):
    if len(m1) != len(m2):
        raise ValueError('Given matrices are not the same size.')
    ref_len = len(m1[0])
    for m in m1:
        if len(m) != ref_len:
            raise ValueError('Given matrices are not the same size.')
    for m in m2:
        if len(m) != ref_len:
            raise ValueError('Given matrices are not the same size.')
    return True


print(lengths_equal(m1, m2))
