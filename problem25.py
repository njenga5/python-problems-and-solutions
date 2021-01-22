'''
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''


class Test:
    parameter = 'Process'

    def __init__(self):
        self.parameter = 'The Haber'


test = Test()
print('%s %s' % (test.parameter, Test.parameter))
