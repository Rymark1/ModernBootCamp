# Doubly linked list is the exact same as a singly linked list, except you can iterate both forwards and backwards.
#  This requires the Nodes to have both a next anda prev 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index > self.length / 2:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        else:
            for _ in range(index):
                temp = self.head.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp


dll = DoublyLinkedList(5)
print("******Testing Append******")
dll.append(10)
dll.append(15)
dll.print_list()
print("******Testing Pop******")
print(dll.pop().value)
print(dll.pop().value)
print(dll.pop().value)
print(dll.pop())
print("******Testing Prepend******")
print(dll.prepend(3))
print(dll.prepend(6))
print(dll.prepend(9))
dll.print_list()
print("******Testing pop_first******")
print(dll.pop_first().value)
print(dll.pop_first().value)
print(dll.pop_first().value)
print(dll.pop_first())
print("******Testing get******")
print(dll.prepend(3))
print(dll.prepend(6))
print(dll.prepend(9))
print(dll.get(2).value)
print(dll.get(4))
print(dll.get(-1))
dll.print_list()
print("******Testing set_value******")
print(dll.set_value(2, 100))
dll.print_list()
print("******Testing insert******")
dll.insert(2, 30)
dll.insert(3, 300)
dll.print_list()
print("******Testing remove******")
dll.remove(2)
dll.print_list()
dll.remove(2)
dll.print_list()