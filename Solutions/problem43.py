'''
Question 43:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

Hints:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.
'''


nums = tuple([i for i in range(1, 11)])
nums2 = tuple([i for i in nums if i % 2 == 0])
print(nums2)
