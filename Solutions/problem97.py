'''
Question 97:

Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

Hints:
Use list[::-1] to iterate a list in a reverse order.
'''

s = input(': ')
s = s[::-1]
print(s)

########################## OR ###################
s = input(': ').split()
for x in range(len(s)):
    print(s[::-1][x][::-1], end=' ')

############################# OR #################
s = input(': ').split()
li = []
for x in s[::-1]:
    li.append(x[::-1])
print(' '.join(li))
