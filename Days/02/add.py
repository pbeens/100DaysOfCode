'''
date: 2019-10-01
name: Peter Beens
description: "Add" challenge from Python Morsels. See screenshot in accompanying README file.
link: https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/ (must have subscription)
'''

debug = True # boolean variable used when I want feeback on some variables

# this should produce [[8, 8], [7, 7]]
sample_data = [[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]]

def add(list_of_lists):
    # first, let's grab the inner lists
    lists = []
    for item in list_of_lists:
        lists.append(item)
    if debug:
        for item in lists:
            print(item)
    # for inner_list in matrix2:
    #     for item in inner_list:
    #         m2_items.append(item)
    # if debug: # warm fuzzy feeling
    #     print(f'list 1: {m1_items}')
    #     print(f'list 2: {m2_items}')

    # do the math and put the sums in a new 1d list
    # sum_list = []
    # for i in range(len(m1_items)):
    #     sum_list.append(int(m1_items[i]) + int(m2_items[i]))
    # if debug: # warm fuzzy feeling
    #     print(f'items added: {sum_list}')

    # extact the individual items from sum_list and parse into lists.
    # list_length = 2
    # new_list_of_lists = [sum_list[x:x+list_length] for x in range(0, len(sum_list), list_length)]
    # if debug: # warm fuzzy feeling
    #     print(f'new list of added items: {new_list_of_lists}')

    # return statement
    # return new_list_of_lists

# statement for main part of challenge
# print(add(matrix1, matrix2))

# Bonus 1 
add(sample_data)

# TODO: I have the lists extracted but now I need to parse them to do the math. I must make sure it works with differing numbers of sub-lists.