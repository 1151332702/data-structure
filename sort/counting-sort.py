# @Time : 2021/4/6 20:08 
# @Author : lilong
# @File : counting-sort.py 
# @Description:  计数排序

#  只适用于只有整数的情况
#  当最大值和最小值相差过大时，会造成空间浪费
#  稳定排序


def counting_sort(arr):
    min_v = min(arr)
    max_v = max(arr)
    diff = max_v - min_v
    count = list()
    # 初始化列表
    [count.append(0) for _ in range(diff + 1)]
    # 统计次数
    for v in arr:
        index = v - min_v
        count[index] = count[index] + 1
    print(count)
    # 累加
    acc = list()
    for i in range(len(count)):
        if i == 0:
            acc.append(count[i])
        else:
            acc.append(count[i] + acc[i - 1])
    print(acc)
    # 排序
    ## 初始化结果列表
    result = list()
    [result.append(0) for _ in range(len(arr))]
    print(result)
    # 组织result
    for v in reversed(arr):
        index = acc[v - min_v]
        result[index - 1] = v
        acc[v - min_v] -= 1

    return result


if __name__ == '__main__':
    a = [3, 3, 1, 2, 5, 5, 7, 5, 6, 5]
    print(counting_sort(a))

