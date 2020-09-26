import random as rand


def partition(a, l, r):
    k = rand.randint(l, r)
    a[l], a[k] = a[k], a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= a[l]:
            a[i], a[j + 1] = a[j + 1], a[i]
            j += 1
    a[l], a[j] = a[j], a[l]
    return j


def sort(a, l, r):
    if r <= l:
        return
    k = partition(a, l, r)
    sort(a, l, k - 1)
    sort(a, k + 1, r)
    return a
