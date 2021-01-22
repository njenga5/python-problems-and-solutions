'''
Question 37:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
'''


def squares(n=21):
    squared = [value**2 for value in range(1, n)]
    return squared


print(squares())
