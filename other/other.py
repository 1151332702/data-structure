# @Time : 2020/10/19 15:55 
# @Author : lilong
# @File : other.py 
# @Description:  一些其他算法


# 数组倒置 减而治之 递归
def reverse_arr(arr, low, high):
    if low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
        reverse_arr(arr, low, high)


# 寻找序列中的最大值和次大值，比较的次数尽可能的少
# 采用分而治之的思想
def find_max_and_next_max(values_list, low, high):
    if low == high:  # 只有一个元素
        return values_list[low], float('-inf')
    if low + 1 == high:  # 两个元素
        return (values_list[low], values_list[high]) if values_list[low] > values_list[high] else (values_list[high], values_list[low])
    mid = (low + high) // 2
    l1, l2 = find_max_and_next_max(values_list, low, mid)
    r1, r2 = find_max_and_next_max(values_list, mid + 1, high)
    if l1 > r1:
        next_max = l2 if l2 > r1 else r1
        return l1, next_max
    else:
        next_max = l1 if l1 > r2 else r2
        return r1, next_max


#  有序列表去重 优化
def delete_duplicated(l):
    i, j = 0, 1
    while j < len(l):
        if l[j] == l[i]:
            j += 1
        else:
            l[i + 1] = l[j]
            i += 1
    return l[: i + 1]


# 二分查找简单版本 直接查询 未查询到返回-1
def bin_search1(l, v, low, high):  # high = size
    while low < high:
        mid = (low + high) // 2
        if v > l[mid]:
            low = mid + 1
        elif l[mid] > v:
            high = mid
        else:
            return mid
    return -1


# 二分查找 返回不大于所要查找的元素v的最后一个位置
def bin_search2(l, v, low, high):  # high = size
    while low < high:
        mid = (low + high) // 2
        if v < l[mid]:
            high = mid
        else:
            low = mid + 1
    return low - 1


if __name__ == '__main__':
    # values = list(range(10))
    # m1, m2 = find_max_and_next_max(values, 0, len(values) - 1)
    # print(m1, m2)
    # v_l = [1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 6]
    # print(delete_duplicated(v_l))
    # print(bin_search2(v_l, 5, 0, len(v_l)))

    a = [1, 2, 3, 4, 5]
    reverse_arr(a, 0, len(a) - 1)
    print(a)
    pass

