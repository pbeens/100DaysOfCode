'''
date: 2019-10-01
name: Peter Beens
description: "Add" challenge from Python Morsels. See screenshot in accompanying README file.
link: https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/ (must have subscription)
'''

debug = False # boolean variable used when I want feeback on some variables

# sample data. Result should be [[3, -3], [-3, 3]].
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

def add(m1, m2):
    # extract the list items and put in new lists
    m1_items = []
    m2_items = []
    for inner_list in matrix1:
        for item in inner_list:
            m1_items.append(item)
    for inner_list in matrix2:
        for item in inner_list:
            m2_items.append(item)
    if debug: # warm fuzzy feeling
        print(f'list 1: {m1_items}')
        print(f'list 2: {m2_items}')

    # do the math and put the sums in a new 1d list
    sum_list = []
    for i in range(len(m1_items)):
        sum_list.append(int(m1_items[i]) + int(m2_items[i]))
    if debug: # warm fuzzy feeling
        print(f'items added: {sum_list}')

    # extact the individual items from sum_list and parse into lists.
    list_length = 2
    new_list_of_lists = [sum_list[x:x+list_length] for x in range(0, len(sum_list), list_length)]
    if debug: # warm fuzzy feeling
        print(f'new list of added items: {new_list_of_lists}')

    # return statement
    return new_list_of_lists

print(add(matrix1, matrix2))

# TODO: Need to add bonus parts of challenge