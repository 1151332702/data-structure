# 冒泡 稳定 时间复杂度o(n^2)
def bubble_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    a = [3, 2, 4, 1]
    bubble_sort(a)
    print(a)
