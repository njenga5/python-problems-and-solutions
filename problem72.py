'''
Question 72:

Write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.
'''

nums = [2, 5, 7, 9, 11, 17, 222]


def search(item):
    if item in nums:
        return nums.index(item)
    raise ValueError('Num is not available in the list')


print(search(222))
