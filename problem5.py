'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''
class Getprint:
    def __init__(self):
        self.word = ''

    def getString(self):
        self.word = input('Enter a word: ')

    def printString(self):
        print(self.word.upper())


value = Getprint()
value.getString()
value.printString()
