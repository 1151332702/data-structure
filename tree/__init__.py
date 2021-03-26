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
                # d = data.pop(0)
                # l_node = None if d is None else BinTree(d)
                l_node = BinTree(data.pop(0))
                node.insert_as_l_child(l_node)
                q.append(l_node)

            if data:
                # d = data.pop(0)
                # r_node = None if d is None else BinTree(d)
                r_node = BinTree(data.pop(0))
                node.insert_as_r_child(r_node)
                q.append(r_node)
        return r

    # 递归实现前序遍历
    # 根 左 右
    def pre_traverse_recursive(self):
        print(self.data)
        if self.l_child:
            self.l_child.pre_traverse_recursive()
        if self.r_child:
            self.r_child.pre_traverse_recursive()

    # 非递归方式实现前序遍历，其实是每一轮迭代都朝着树的左下进行，每次都进行访问
    @ staticmethod
    def pre_traverse(node):
        stack = Stack()
        while True:
            while node:
                print(node.data)
                stack.push(node.r_child)
                node = node.l_child
            if stack.is_empty():
                break
            node = stack.pop()

    # 递归方式实现中序遍历
    # 左 根 右
    @staticmethod
    def mid_traverse_recursive(node):
        if node.l_child:
            BinTree.mid_traverse_recursive(node.l_child)
        print(node.data)
        if node.r_child:
            BinTree.mid_traverse_recursive(node.r_child)

    # 非递归方式实现中序遍历，每轮遍历依然是往左下进行，进行的过程中不会访问，而是依次入栈
    @staticmethod
    def mid_traverse(node):
        stack = Stack()
        while True:
            while node:
                stack.push(node)
                node = node.l_child
            if stack.is_empty():
                break
            node = stack.pop()
            print(node.data)
            node = node.r_child

    # 递归实现后续遍历
    def post_traverse_recursive(self):
        if self.l_child:
            self.l_child.post_traverse_recursive()
        if self.r_child:
            self.r_child.post_traverse_recursive()
        print(self.data)

    # 非递归方式实现后序遍历
    @staticmethod
    def post_traverse(node):
        stack = Stack()
        stack.push(node)
        while not stack.is_empty():
            if stack.top() is not node.parent:  # 栈顶节点不是当前节点的parent，则必为当前节点的右兄节点
                while stack.top().l_child or stack.top().r_child:
                    node = stack.top()
                    if node.r_child:
                        stack.push(node.r_child)
                    if node.l_child:
                        stack.push(node.l_child)
            node = stack.pop()
            print(node.data)

    # 层次遍历
    def traverse_level(self):
        quque = list()
        quque.insert(0, self)  # 根节点入队列
        while quque:
            node = quque.pop(0)
            print(node.data)
            if node.l_child:
                quque.append(node.l_child)
            if node.r_child:
                quque.append(node.r_child)


if __name__ == '__main__':
    tree = BinTree.build_tree([0, 1, 2, 3, 4, 5, 6])
    # tree.pre_traverse_recursive()
    # BinTree.pre_traverse(tree)
    # BinTree.mid_traverse_recursive(tree)
    # BinTree.mid_traverse(tree)
    # tree.post_traverse_recursive()
    # BinTree.post_traverse(tree)
    tree.traverse_level()