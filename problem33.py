'''
Question 33:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
'''


def squares(n=4):
    squared = {key: key**2 for key in range(1, n)}
    return squared


print(squares())
