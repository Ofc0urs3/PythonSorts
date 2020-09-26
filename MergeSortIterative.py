def merge(a, tmp, start, mid, end):
    k = start
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if a[i] < a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1
    while i <= mid and i < len(a):
        tmp[k] = a[i]
        k += 1
        i += 1
    for i in range(start, end + 1):
        a[i] = tmp[i]


def sort(a, start, end):
    m = 1
    tmp = [0] * len(a)
    for i in range(0, len(a)):
        tmp[i] = a[i]

    while m <= end - start:
        for i in range(start, end, 2 * m):
            left = i
            mid = i + m - 1
            right = min(i + 2 * m - 1, end)
            merge(a, tmp, left, mid, right)
        m *= 2
    return a
