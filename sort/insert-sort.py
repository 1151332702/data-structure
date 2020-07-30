# 插入排序 稳定 时间复杂度o(I + n)
# I是逆序对的数目
# 插入排序可以理解为对无序的修复。逆序对越多，需要做的修复工作也越多，时间复杂度也就越高。
# 插入排序适合于使用链表，插入的复杂度为o(1)


def insert_sort(arr):
    result = [arr.pop(0)]
    for _ in range(len(arr)):
        v = arr.pop(0)
        for j in range(len(result)):
            if v <= result[j]:
                result.insert(j, v)
                break
            else:
                if j == len(result) - 1:
                    result.append(v)
    return result


# 插入排序是输入敏感的排序算法，他的复杂度不仅取决于n，同样取决于输入的值。
if __name__ == '__main__':
    a = [3, 2, 4, 1]
    r = insert_sort(a)
    print(r)
