# 二叉树
from stack import Stack


class BinTree(object):
    def __init__(self, data, parent=None, l_child=None, r_child=None):
        self.data = data
        self.parent = parent
        self.l_child = l_child
        self.r_child = r_child

    def insert_as_l_child(self, e):
        self.l_child = e
        e.parent = self

    def insert_as_r_child(self, e):
        self.r_child = e
        e.parent = self

    def size(self):
        s = 1
        if self.l_child is not None:
            s += self.l_child.size()
        if self.r_child is not None:
            s += self.r_child.size()
        return s

    # 传递列表 构建二叉树
    @staticmethod
    def build_tree(data):
        if not data:
            return None
        q = list()
        r = BinTree(data.pop(0))
        q.append(r)
        while q:
            node = q.pop(0)
            if data:
                l_node = BinTree(data.pop(0))
                node.l_child = l_node
                q.append(l_node)

            if data:
                r_node = BinTree(data.pop(0))
                node.r_child = r_node
                q.append(r_node)
        return r

    # 递归实现前序遍历
    # 中 左 右
    def pre_traverse_recursive(self):
        print(self.data)
        if self.l_child:
            self.l_child.pre_traverse_recursive()
        if self.r_child:
            self.r_child.pre_traverse_recursive()

    # 非递归方式实现前序遍历
    @ staticmethod
    def pre_traverse(node):
        stack = Stack()
        stack.push(node)
        while not stack.is_empty():
            tmp_node = stack.pop()
            print(tmp_node.data)
            if tmp_node.r_child:
                stack.push(tmp_node.r_child)
            if tmp_node.l_child:
                stack.push(tmp_node.l_child)

    # 递归方式实现中序遍历
    # 左 中 右
    @staticmethod
    def mid_traverse_recursive(node):
        if node.l_child:
            BinTree.mid_traverse_recursive(node.l_child)
        print(node.data)
        if node.r_child:
            BinTree.mid_traverse_recursive(node.r_child)

    # 非递归方式实现中序遍历
    @staticmethod
    def mid_traverse(node):
        stack = Stack()
        stack.push(node)
        while stack:
            while node.l_child:
                node = node.l_child
                stack.push(node)
            print(stack.pop().data)
            node = stack.pop()
            print(node.data)
            while node.r_child is None:
                node = stack.pop()
                print(node.data)
            print(node.data)
            node = node.r_child
            stack.push(node)



if __name__ == '__main__':
    tree = BinTree.build_tree([0, 1, 2, 3, 4, 5, 6])
    # tree.pre_traverse_recursive()
    # BinTree.pre_traverse(tree)
    # BinTree.mid_traverse_recursive(tree)
    BinTree.mid_traverse(tree)
