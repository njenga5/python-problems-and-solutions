'''
Question 64:

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float
'''

# num = int(input(': '))
# quotients = []
# for i in range(1, num+1):
#     quotients.append(i/(i+1))
# result = 0
# for x in quotients:
#     result += x

# print('Result = %f' % (result))

####################### OR ##################

num = int(input(': '))
sum = 0
for i in range(1, num+1):
    sum += float(i)/(i + 1)

print('Sum = %4f' % sum)
