#  Terminology to remember: Unfull, full, perfect, complete, parent node, child node, sibling nodes
#
#  A tree is a node that points to any number of Nodes.  In our example, we are making a binary tree which points to
#  exactly 2 nodes.  If every node points to zero nodes or 2 nodes, the tree is considered full.  If any of the node
#  don't point to zero or the max number of nodes, it is considered unfull.  A perfectly full tree, requires each
#  level of Nodes to be maxed out. For example:
#               A Full tree        An unfull tree          A Perfect Tree
#                     4                 4                       4000
#                    / \               / \                     /    \
#                   3   5             3   5                   3      5
#                  / \               /                       / \    / \
#                 12  7             12                      12  7  9  10
#
#  A perfect tree is also called a complete tree.
#
#          4  <- Parent node
#         / \
#        5   6 <- Child node  (5 and 6 are sibling Nodes)
#
#   Children nodes can be parent nodes to a lower level of Nodes.
#
#
#   A binary search tree takes an initial node and then for any new value that is greater than, it appends to the
#   right side, less than on the left.  Assume the nodes are 47, 76, 52, 21, 82, 18, 27 in that order.
#   Below will be how the graph gets built by step.
#
#         47               76             52             21            82              18                 27
#       Step 1          Step 2          Step 3         Step 4       Step 5           Step 6             Step 7
#         47              47              47             47           47               47                   47
#                           \               \           /  \         /  \             /  \                /    \
#                            76              76       21    76     21    76         21    76            21      76
#                                           /              /            /  \       /     /  \          /  \    /  \
#                                          52            52           52   82     18   52   82       18   27  52   82
#
#   Every child on the left is considered less than the parent, and every child on the right is considered greater
#   than the parent.
#
#   Binary search tree O(log n) which is very efficient.  with 4 levels, there are 2^n - 1 nodes where n = levels.
#   Since 1 in a constant, we remove it and now we have 2^n, which then in terms of search capibilities, turns into
#   log(n).
#   Worst case for a tree would be a tree with all children being greater than the parent, which would essentially be a
#   linked list which would result in O(n).

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains_value(self, value):
        if self.root is None:
            return False

        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.left
        return False


my_tree = BinarySearchTree()
print(my_tree.insert(2))
print(my_tree.insert(1))
print(my_tree.insert(3))
print(my_tree.insert(3))
print(my_tree.root.value)
