# @Time : 2020/10/20 11:20 
# @Author : lilong
# @File : fib.py 
# @Description:


# 时间复杂度2^n 非常耗时
# 内部包含大量的重复计算
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


# 优化方案A 记录中间结果
def fib2(n, r):
    if n in r:
        return r[n]
    if n == 0 or n == 1:
        return n
    r[n - 1] = fib2(n - 1, r)
    r[n - 2] = fib2(n - 2, r)
    return r[n - 1] + r[n - 2]


# 优化方案B 动态规划 自底向上
def fib3(n):
    a, b = 0, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b


if __name__ == '__main__':
    d = dict()
    print(fib3(64))
