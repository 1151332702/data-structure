# @Time : 2020/10/19 15:55 
# @Author : lilong
# @File : other.py 
# @Description:  一些其他算法


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


if __name__ == '__main__':
    # values = list(range(10))
    # m1, m2 = find_max_and_next_max(values, 0, len(values) - 1)
    # print(m1, m2)

    pass

