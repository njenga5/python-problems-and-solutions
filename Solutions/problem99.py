'''
Question 99:

Please write a program which prints all permutations of [1,2,3]


Hints:
Use itertools.permutations() to get permutations of list.
'''

from itertools import permutations
with open('a.txt', 'w')as f:
    print(list(permutations([1, 2, 3])), file=f)
    for value in permutations([1, 2, 3]):
        print(value, end=' ', file=f)
