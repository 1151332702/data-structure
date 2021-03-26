# @Time : 2021/3/25 11:12 
# @Author : lilong
# @File : bst.py 
# @Description:
from tree import BinTree

# bst搜索，实际上就是二分查找，实际返回定位到的节点以及父节点
def bst_search(node, data, f_node=None):
    if node.data == data or node.data is None:
        return node, f_node
    else:
        return bst_search(node.l_child, data, node) if node.data > data else bst_search(node.r_child, data, node)

# 这里所构建的bst树中的空节点其实是data为None的BinTree节点
# 插入实际上就是把搜索接口返回的定位到的节点指向索要插入的点
def bst_insert(node, data):
    s_node, f_node = bst_search(node, data)
    s_node.data = data
    print(f_node)

# 删除：如果待删除的节点的右子树为空，那么就把左子树连接到其父节点；如果左子树为空，那么就把右子树连接到其父节点；如果有两个子树，
# 情况稍微复杂，需要把待删除的节点与其直接后继交换位置，交换之后如果待删除的节点没有子树，直接删除，如果有（只能是一个右子树），
# 删除之后把其右子树放在已删除节点的位置

# bst不平衡时可以通过一定的算法转换成bbst


##   avl树
# avl树：任意一个节点两个子树的高度差<=1，是一种适度平衡的bst。
# avl可以直接使用bst的搜索接口，但是插入和删除接口需要重构，因为插入或者删除之后，接口可能变得不平衡了
# 插入一个节点，可能会导致失衡的节点：父节点以及祖先节点，其他节点不会失衡
# 删除一个节点，可能会导致失衡的节点：只有这个节点的父节点
# 插入一个节点导致的失衡，通过旋转来进行重平衡。而且子节点的修复成功之后，父节点的失衡也随之修复（修复后的子树高度不变）
# 由于删除节点导致的失衡，也是通过旋转来进行调整，但是调整之后，子树的高度可能会改变，因此可能会导致更高的祖先节点失衡，需要对祖先再次进行旋转，
# 最差需要旋转o(log n)次
# 所谓各种方式的旋转本质就是3 + 4重平衡，3是指失衡节点紧随其后的两个较高的节点，4是指4棵子树。所要做的其实就是把3个节点放在4棵子树中间。
# avl树优点：无论是查找，插入还是删除，时间复杂度最坏都是log n，使用了n的存储空间
# 缺点：借助了高度和平衡因子，需要改造元素的结构，或者额外封装；删除操作最多需要进行log n次转；

##   伸展树
# 我们访问了某个节点，该节点很大概率还会被接着访问。所以在bst中可以通过一种策略把刚刚被访问的节点放在更容易被搜索到的位置，比如树根处：通过旋转
# 的方式使得该被访问的节点逐层上升，动态来看就是一棵树不断进行伸展的过程
# 一种使得节点逐层上升的方式是：每次不只关注他的父节点，还有他的祖先节点，三个节点旋转2次使得该节点到达祖先节点的位置，第一次旋转使得该节点和父亲
# 节点上升一层，祖父节点下降一层，第二次旋转使得子节点上升一层。通过这种旋转方式在某种情况下可以使得树的深度变浅，从而优化bst的性能。
# 伸展树的查找接口：如果找到，把找到的节点上升到根节点；如果未找到，空节点位置处的父节点上升到根节点
# 伸展树的新增接口，先调用查找接口，（未找到），完成之后树已经进行的伸展，只要把节点新增在树的根节点即可
# 删除接口，先调用查找接口，该节点上升到根节点，删除根节点（找到根节点的直接后继作为新的根节点）

##   B树
# 平衡的多路搜索树，经过适当合并，得到超级节点。每两代合并：4路；每3代合并：8路；每d代合并，m=2^d路，有m-1个关键码
# 假如有1g的记录，每次查找需要进行log 2 10^9 = 30次io，每次只能读出一个k，每次io都非常耗时，得不偿失。但是B树每次可以读出一组超级key，这一组
# key包含m-1个值。每组超级key的数目取决于：磁盘数据块的大小 / 每个key的大小。尽量保证每次io拿到一个数据块的数据
# B树路数为m，每个节点的分支数的上下界为【m/2, m】，m / 2取上界




if __name__ == '__main__':
    tree = BinTree.build_tree([16, 10, 25, 5, 11, 19, 28, 2, 8, None, 15, 17, 22, 27, 37, None, 4, None, None, 13, None, None, None, None, None, None, None, 33, None])
    # print(tree)
    n, f = bst_search(tree, 40)
    # print(n, f)
    # bst_insert(tree, 40)

