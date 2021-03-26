# @Time : 2021/3/24 15:45 
# @Author : lilong
# @File : __init__.py.py 
# @Description:
from enum import Enum


class GStatus(Enum):
    UNDISCOVERED = 0
    DISCOVERED = 1
    VISITED = 2


class EStatus(Enum):
    UNDETERMINED = 0
    TREE = 1
    CROSS = 2
    FORWARD = 3
    BACKWARD = 4


class Graph():
    def __init__(self, data):
        self.data = data
        self.in_degree = 0  # 入度
        self.out_degree = 0  # 出度
        self.status = GStatus.UNDISCOVERED
        self.d_time = -1
        self.f_time = -1
        self.parent = -1
        self.priority = float('inf')


class Edge():
    def __init__(self, data, weight):
        self.data = data
        self.weight = weight
        self.status = EStatus.UNDETERMINED


# 广度优先搜索 等同于 树的层次遍历。广度优先搜索的结果就是一个极大无环图，也就是树
# 利用队列实现，每次都把相邻顶点入队列


