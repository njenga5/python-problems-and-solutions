
'''
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

items = input(': ')
d = {'UPPER CASE':0, 'LOWER CASE':0}

for i in items:
    if i.isalpha() and i.isupper():
        d['UPPER CASE'] += 1
    elif i.isalpha() and i.islower():
        d['LOWER CASE'] += 1

print('UPPER CASE',d['UPPER CASE'])
print('LOWER CASE',d['LOWER CASE'])
