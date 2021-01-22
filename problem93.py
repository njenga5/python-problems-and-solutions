'''
Question 93:

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.
'''

values = set([1, 3, 6, 78, 35, 55])
values_2 = set([12, 24, 35, 24, 88, 120, 155])
values &= values_2
li = list(values)
print(li)
