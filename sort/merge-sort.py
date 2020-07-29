# 归并  时间复杂度o(nlogn)
def merge(arr, low, mid, high):
    a1 = arr[low: mid + 1]
    a2 = arr[mid + 1: high + 1]
    r = []
    while len(a1) != 0 and len(a2) != 0:
        if a1[0] <= a2[0]:
            r.append(a1.pop(0))
        else:
            r.append(a2.pop(0))
    if len(a1) != 0:
        r.extend(a1)
    if len(a2) != 0:
        r.extend(a2)
    arr[low: high + 1] = r


def merge_sort(arr, low, high):
    if low == high:
        return
    mid = (low + high) // 2  # mid包含在前半区间
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)


if __name__ == '__main__':
    a = [3, 2, 4, 1, 6]
    merge_sort(a, 0, len(a) - 1)
    print(a)