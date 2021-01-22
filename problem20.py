'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

'''


class Iterator:
    def __init__(self, n):
        self.n = n

    def putNumbers(self):
        i = 0
        while i < self.n:
            j = i
            i += 1
            if j % 7 == 0:
                yield j


test = Iterator(100)
div_by_seven = []
for i in test.putNumbers():
    div_by_seven.append(i)

print(div_by_seven)
