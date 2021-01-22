'''
Question 48:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''

nums = [i for i in range(1, 21)]
nums2 = list(filter(lambda x: x % 2 == 0, nums))
print(nums2)
