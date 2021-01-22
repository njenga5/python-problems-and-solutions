'''
Question 57:
Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.
'''


class Custom(Exception):
    '''
        My custom exception class
    Attributes:
        message -- Explanation of the exception
    '''
    message = 'This is a custom exception'

    def __init__(self, message):
        self.message = message


print(Custom.message)
print(Custom('Exception'))
