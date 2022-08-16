import random
from random import randint

a = [randint(0, 10000000000000000) for i in range(10000)]
b = a.copy()


def quickSort(alist):
    if not alist:
        return alist
    pivot = random.choice(alist)
    equalList = []
    smallerList = []
    biggerList = []

    for item in alist:
        if item < pivot:
            smallerList.append(item)
        elif item == pivot:
            equalList.append(item)
        else:
            biggerList.append(item)
    return quickSort(biggerList) + equalList + quickSort(smallerList)


def my_sort(arr: list):
    length = len(arr)
    flag = start = 0

    if length <= 1:
        return arr

    for my_index in range(length):
        if arr[start] > arr[my_index]:
            flag += 1
            arr[flag], arr[my_index] = arr[my_index], arr[flag]

    arr[flag], arr[start] = arr[start], arr[flag]

    return my_sort(arr[:flag]) + my_sort(arr[flag:flag + 1]) + my_sort(arr[flag + 1:])



import time
start_t = time.time()
quickSort(b)
print(time.time() - start_t)


start_t = time.time()
my_sort(a)
print(time.time() - start_t)


