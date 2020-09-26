import HeapSort
import MergeSortIterative
import MergeSortRecursive
import QuickSort
import doctest
import random as rand
import time

# Функция принимает на вход имя файла, в котором содержится последовательность чисел, сортирует все положительные числа
# оставляя остальные в начале массива в исходном порядке
def change_list(s, sorting):
    """
    >>> g = open("f1.txt", 'w')
    >>> g.write("")
    0
    >>> change_list("1.txt", QuickSort)
    -1
    >>> g = open("2.txt", 'w')
    >>> g.write(" 1 2 a")
    6
    >>> g.close()
    >>> change_list("2.txt", QuickSort)
    -2
    >>> g = open("3.txt", 'w')
    >>> g.write("5 -1 4 -2 3 -3 2 -4 1 -5")
    24
    >>> g.close()
    >>> change_list("3.txt", QuickSort)
    [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]
    >>> change_list("kjsndf.txt", QuickSort)
    -1
    >>> g = open("f.txt", 'w')
    >>> g.write("-5 -1 -4 -2 -3 -3 -2 -4 -1 -5")
    29
    >>> g.close()
    >>> change_list("f.txt", QuickSort)
    [-5, -1, -4, -2, -3, -3, -2, -4, -1, -5]
    """
    a = []
    n = 0
    try:
        f = open(s, "r")
    except FileNotFoundError:
        return -1  # file not found error
    for line in f:
        for k in line.split(" "):
            for s in k.split("\n"):
                if s == '':
                    continue
                try:
                    c = int(s)
                except ValueError:
                    f.close()
                    return -2  # value error
                a.append(c)
                n += 1
    f.close()
    if n == 0:
        return -3  # file empty

    j = 0

    neg_count = 0
    for i in range(n):
        if a[i] <= 0:
            while i != j and a[j] <= 0:
                j += 1
            a[i], a[j] = a[j], a[i]
            j += 1
            neg_count += 1
    if neg_count == len(a):
        return a

    return sorting.sort(a, neg_count, n - 1)  # Тут менять тип сортировки


def check(a):
    neg = 0
    while neg < len(a) and a[neg] <= 0:
        neg += 1
    if neg == len(a):
        return 1
    prev = a[neg]
    for i in range(neg, len(a)):
        if a[i] <= 0:
            return 0
        if a[i] < prev:
            return 0
        prev = a[i]
    return 1


def test_time():
    print("Enter n:")
    n = int(input())
    f = open("time_test.txt", 'w')
    for i in range(n):
        f.write(str(rand.randint(-100, 100)) + " ")
    f.close()
    start_time = time.time()
    change_list("time_test.txt", QuickSort)
    print("QuickSort time: " + str(time.time() - start_time))
    start_time = time.time()
    change_list("time_test.txt", HeapSort)
    print("HeapSort time: " + str(time.time() - start_time))
    start_time = time.time()
    change_list("time_test.txt", MergeSortIterative)
    print("MergeSortIterative time: " + str(time.time() - start_time))
    start_time = time.time()
    change_list("time_test.txt", MergeSortRecursive)
    print("MergeSortRecursive time: " + str(time.time() - start_time))


doctest.testmod()
test_time()
res = change_list("f.txt", QuickSort)
if res == -1:
    print("File not found")
elif res == -2:
    print("Value error")
elif res == -3:
    print("File empty")
else:
    print(res)
    print("check: " + str(check(res)))
