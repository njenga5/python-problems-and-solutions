'''
Question 75:

Please generate a random float where the value is between 5 and 95 using Python math module.



Hints:
Use random.random() to generate a random float in [0,1].
'''


from random import random
rand = random()*100
if 5 <= rand <= 95:
    print(rand)
