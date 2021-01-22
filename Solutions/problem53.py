'''
Question 53:
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.
'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculateArea(self):
        return (self.length * self.width)


rect = Rectangle(3, 4)
print(rect.calculateArea())