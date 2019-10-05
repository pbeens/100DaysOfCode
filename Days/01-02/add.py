'''
date: 2019-09-30
name: Peter Beens
description: "Add" challenge from Python Morsels. See screenshot in accompanying README file.
link: https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/ (must have subscription)
'''

debug = False  # boolean variable used when I want feeback on some variables


def add(m1, m2):
    # extract the list items and put in new lists
    m1_flattened = [n for row in m1 for n in row]
    m2_flattened = [n for row in m2 for n in row]

    # create a list of the sums (should produce [3, -3, 3, 3] from test data)
    sum_list = [x + y for x, y in zip(m1_flattened, m2_flattened)]
    if debug:
        print(sum_list)
    sum_to_matrix = [sum_list[i:i + 2] for i in range(0, len(sum_list), 2)]

    # return statement
    return sum_to_matrix


# test 1 result should be [[3, -3], [-3, 3]]
print(add([[1, -2], [-3, 4]],
          [[2, -1], [0, -1]]))

# test 2 result should be [[3, -3], [-3, 3], [3, -3], [-3, 3]]
print(add([[1, -2], [-3, 4], [1, -2], [-3, 4]],
          [[2, -1], [0, -1], [2, -1], [0, -1]]))

# test 3 should be [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
print(add([[1, -2, 3], [-4, 5, -6], [7, -8, 9]],
          [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]))

# TODO: Need to adapt function to work with len(sub-lists) != 2
