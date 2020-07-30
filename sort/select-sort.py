# 选择 不稳定 时间复杂度o(n^2)
def select_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 选择排序的效率优于冒泡排序，冒泡排序在每一轮交换中都大概率进行多次数据交换
# 但是选择排序在每一轮中只需要进行一次数据交换
if __name__ == '__main__':
    a = [3, 2, 4, 1]
    select_sort(a)
    print(a)
