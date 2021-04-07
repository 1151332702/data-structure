# @Time : 2021/4/7 14:25 
# @Author : lilong
# @File : bucket-sort.py 
# @Description:  桶排序

# 把数据分到若干个桶内，对桶内的数据进行排序，最后输出桶内的数据
# 复杂度分析：m个桶，每个桶内的元素平均为n / m, 初始化桶：m；最大最小值：n；元素入桶：n，所有桶内元素排序：m * n/m * log (n/m)；输出：n
# 加起来3n + m + n*log(n/m). 当m == n时，总体复杂度为o(n + m)
# 当元素分布比较均匀时可以使用这种方法。极限情况下元素大部分分布于某个桶内，时间复杂度退化为o(nlogn)
import math


# 递归实现 快速排序
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


def bucket_sort(arr):
    # 配置桶的数量和数组的数量相同并初始化桶
    bucket = list()
    [bucket.append(list()) for _ in range(len(arr))]

    min_v = min(arr)
    max_v = max(arr)
    span = (max_v - min_v) / len(arr)
    # 数据入桶
    for v in arr:
        bucket_no = math.ceil((v - min_v) / span) - 1
        if bucket_no == -1:
            bucket_no = 0
        bucket[bucket_no].append(v)
    # 对每个桶内的数据进行排序，复杂度nlogn
    for bucket_data in bucket:
        if len(bucket_data) >= 2:
            quick_sort_recursive(bucket_data, 0, len(bucket_data))
    # 组织结果
    result = list()
    for bucket_data in bucket:
        result.extend(bucket_data)

    return result


if __name__ == '__main__':
    a = [4.5, 0.84, 3.25, 2.18, 0.5]
    print(bucket_sort(a))