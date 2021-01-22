'''
Question 96:

Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.
'''

freq = dict()
s = input(': ')
val = set()
for l in s:
    freq[l] = s.count(l)
    val.add(l + ',' + str(freq[l]))
val = sorted(list(val))
for v in val:
    print(v)
