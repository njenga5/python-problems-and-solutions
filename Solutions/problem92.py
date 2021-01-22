'''
Question 92:

By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.
'''
values = [12, 24, 35, 24, 88, 120, 155]
values = [x for x in values if x != 24]
print(values)
