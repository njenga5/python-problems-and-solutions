'''
Question 69:

Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.
'''


def numsGen(n):
    for i in range(0, n):
        yield i


n = int(input(': '))
req_nums = [str(x) for x in numsGen(n) if x % 5 == 0 and x % 7 == 0]
print(','.join(req_nums))
