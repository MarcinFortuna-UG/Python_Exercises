# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []

# You can assume that all values are integers. Do not mutate the input array.

def invert_1(lst):
    return [-el for el in lst]

def invert_2(lst):
    new_lst = []
    for el in lst:
        new_lst.append(el * -1)
    return new_lst
