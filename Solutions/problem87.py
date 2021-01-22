'''
Question 87:
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.
'''

li = [5, 6, 77, 45, 22, 12, 24]
li = list(filter(lambda x: x % 2 != 0, li))
print(li)

######################### OR ##############################
li = [5, 6, 77, 45, 22, 12, 24]
li2 = [x for x in filter(lambda x: x % 2 != 0, li)]
print(li2)

######################### OR ###############################
li = [5, 6, 77, 45, 22, 12, 24]
li2 = [x for x in li if x % 2 != 0]
print(li2)
