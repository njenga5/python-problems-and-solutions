'''
Question 44:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.
'''

value = input(': ')
if value == 'yes' or value == 'Yes' or value == 'YES':
    print('Yes')
else:
    print('No')
