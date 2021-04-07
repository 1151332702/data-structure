# @Time : 2021/4/6 19:00 
# @Author : lilong
# @File : quick-sort.py 
# @Description: 快速排序

#  每轮都选定一个基准元素，比该元素大的移动到该元素的右边，比该元素小的移动到左边。
#  时间复杂度平均o(n logn)，最差o(n ^ 2)
#  不稳定的排序算法


# 递归实现
def quick_sort_recursive(arr, low, high):
    if low == high:
        return
    pivot = arr[low]  # 采用第一个元素作为中间点
    pivot_ind = low
    for ind in range(low + 1, high):
        if arr[ind] <= pivot:
            arr[pivot_ind], arr[ind] = arr[ind], arr[pivot_ind]
            pivot_ind = ind
    quick_sort_recursive(arr, low, pivot_ind)
    quick_sort_recursive(arr, pivot_ind + 1, high)


# 非递归实现
def quick_sort(arr, low, high):
    stack = list()
    stack.append((low, high))
    while stack:
        indices = stack.pop()
        low = indices[0]
        high = indices[1]
        if low == high:
            continue
        pivot = arr[low]  # 采用第一个元素作为中间点
        pivot_ind = low
        for ind in range(low + 1, high):
            if arr[ind] <= pivot:
                arr[pivot_ind], arr[ind] = arr[ind], arr[pivot_ind]
                pivot_ind = ind
        stack.append((low, pivot_ind))
        stack.append((pivot_ind + 1, high))


if __name__ == '__main__':
    a = [3, 2, 1, 6, 5, 4, 9, 8, 7]
    # quick_sort_recursive(a, 0, len(a))
    quick_sort(a, 0, len(a))
    print(a)

