'''
Question 50:
Define a class named African which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
'''


class African:
    @staticmethod
    def printNationality():
        print('Kenyan')


anAfrican = African()
anAfrican.printNationality()
African.printNationality()
