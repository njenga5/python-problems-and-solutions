'''
Question 68:

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.
'''


def evenGen(n):
    for i in range(n):
        yield i


n = int(input(': '))
even_nums = [str(x) for x in evenGen(n) if x % 2 == 0]
print(','.join(even_nums))
