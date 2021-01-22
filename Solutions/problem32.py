'''
Question 32:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
'''


def odd_even(n):
    if n % 2 == 0:
        return 'It is an even number'
    return 'It is an odd number'


print(odd_even(8))
