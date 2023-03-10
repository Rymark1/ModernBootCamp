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

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
            return current_node

    def min_value(self, current_node):
        if current_node.left is None:
            return current_node.value
        current_node = self.min_value(current_node.left)
        return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)



# my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)QQQQQQQQ
# my_tree.insert(82)
#
# print("BST Contains 27:")
# print(my_tree.r_contains(27))
#
# print("\nBST Contains 27:")
# print(my_tree.r_contains(17))

my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
my_tree.r_insert(5)
my_tree.r_insert(7)
print(f"Root: {my_tree.root.value}")
print(f"Root -> Left: {my_tree.root.left.value}")
print(f"Root -> Right: {my_tree.root.right.value}")
print(my_tree.min_value(my_tree.root))

my_tree.delete_node(2)
print(f"Root: {my_tree.root.value}")
print(f"Root -> Left: {my_tree.root.left.value}")
print(f"Root -> Right: {my_tree.root.right.value}")
print(my_tree.min_value(my_tree.root))
