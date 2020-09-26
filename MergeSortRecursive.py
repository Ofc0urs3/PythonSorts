def merge(a, b):
    res = [0] * (len(a) + len(b))
    i = k = l = 0
    while i < len(a) or k < len(b):
        if i < len(a) and k < len(b):
            if a[i] <= b[k]:
                res[l] = a[i]
                i += 1
            else:
                res[l] = b[k]
                k += 1
        else:
            if i < len(a):
                res[l] = a[i]
                i += 1
            else:
                res[l] = b[k]
                k += 1
        l += 1
    return res


def merge_sort(a, l, r):
    m = (l + r) // 2
    if r == l:
        return [a[l]]
    return merge(merge_sort(a, l, m), merge_sort(a, m + 1, r))


def sort(a, l, r):
    if l == 0:
        left = []
    else:
        left = [a[i] for i in range(0, l)]
    if r == len(a) - 1:
        right = []
    else:
        right = [a[i] for i in range(r + 1, len(a))]

    mid = [a[i] for i in range(l, r + 1)]
    return left + merge_sort(mid, 0, len(mid) - 1) + right