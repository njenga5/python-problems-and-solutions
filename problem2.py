def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)

res = factorial(8)
print(res)
