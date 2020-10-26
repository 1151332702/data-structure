# @Time : 2020/10/20 15:14 
# @Author : lilong
# @File : lcs.py 
# @Description:


#  最长公共子序列
#  递归实现 性能较差。包含大量的重复计算 时间复杂度2^n
def lcs1(s1, s2):
    if s1 == '' or s2 == '':
        return 0
    if s1[-1] == s2[-1]:
        return lcs1(s1[: -1], s2[: -1]) + 1
    else:
        return max(lcs1(s1[: -1], s2), lcs1(s1, s2[: -1]))


# 动态规划实现，记录中间结果
def lcs2(s1, s2):
    result = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                result[i][j] = result[i - 1][j - 1] + 1
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])
    for i in range(len(result)):
        print(result[i])
    return result[-1][-1]


if __name__ == '__main__':
    print(lcs2('daslhjgh', 'djkslhh'))
