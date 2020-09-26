def sort(a, start, end):
    build_heap(a, start, end)
    for i in range(end, start - 1, -1):
        a[i] = extract_max(a, start, i)
    return a


def build_heap(a, start, end):
    for i in range((end - start + 1) // 2, -1, -1):
        sift_down(a, i, start, end)


def sift_down(a, i, start, end):
    while start + 2 * i + 1 <= end and ((start + 2 * i + 2 <= end and a[start + 2 * i + 2] > a[start + i]) or a[start + 2 * i + 1] > a[start + i]):
        if start + 2 * i + 2 <= end and a[start + 2 * i + 2] > a[start + 2 * i + 1]:
            a[start + i], a[start + 2 * i + 2] = a[start + 2 * i + 2], a[start + i]
            i = 2 * i + 2
        else:
            a[start + i], a[start + 2 * i + 1] = a[start + 2 * i + 1], a[start + i]
            i = 2 * i + 1


def extract_max(a, start, end):
    max = a[start]
    a[start] = a[end]
    sift_down(a, 0, start, end - 1)
    return max

