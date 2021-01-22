'''
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''


items = input(': ')
d = {'DIGITS':0, 'LETTERS':0,}
for i in items:
    if i.isdigit():
        d['DIGITS'] += 1
    elif i.isalpha():
        d['LETTERS'] += 1

print('LETTERS',d['LETTERS'])
print('DIGITS',d['DIGITS'])


# items = [x for x in input(': ').split()]
# nums = [str(x) for x in range(10)]
# special_char = ['!','@','#','$','%']
# digits = []
# letters = []
# for i in items:
#     for j in i:
#         if j in nums:
#             digits.append(j)
#         elif j not in special_char:
#             letters.append(j)
# print('LETTERS', len(letters))
# print('DIGITS', len(digits))
