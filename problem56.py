'''
Question 56:
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.
'''

try:
    5/0
except ZeroDivisionError as e:
    print('Cannot divide by zero')
