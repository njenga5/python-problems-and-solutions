'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# res = []
# for j in range(1000,3001):
#     for k in str(j):
#         if int(k)%2 == 0:
#             res.append(str(j))
# print(','.join(res))



res = []
for j in range(1000,3001):
    d = str(j)
    if int(d[0])%2 == 0 and int(d[1])%2 == 0 and int(d[2])%2 == 0 and int(d[3])%2 == 0:
            res.append(d)
print(','.join(res))
