'''
Question 70:

Write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.
'''

even_nums = [2, 4, 6, 8]
for i in even_nums:
    assert(i % 2 == 0)
