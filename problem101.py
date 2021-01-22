def f(list1, list2):
    return [x for x in list1 if x in list2]


list1 = [i for i in range(1, 10)]
list2 = [1, 2, 3, 5, 7, 0]
print(f(list1, list2))
