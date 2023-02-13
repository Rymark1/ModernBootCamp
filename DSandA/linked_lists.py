# Linked lists are linked in 1 direction.  There is a head and a tails node.
# A node is really just a dictionary with a piece of data and pointer to let us know which is the next node.
# The Head and Tail attributes "point" to the first and last node of a list and can shift based on appends or deletes.

# The structure underneath the hood looks like:

# some_linked_list = {
#     "value": 11,  # A  Which is the current Head
#     "next": {
#         "value": 3,  # B
#         "next": {
#             "value": 23,  # C
#             "next": {
#                 "value": 7,  # D
#                 "next": {
#                     "value": 50,  # E  Which is the current Tail
#                     "next": None
#                     }
#                 }
#             }
#         }
#     }

# So node A -> B -> C -> D, and in this case Node A is the head and node D is the tails.
# If we append F to the front of the list, F -> A -> B -> C -> D, node F becomes the new Head, and we update node F
# to point to Node A.
# This insertion/prepend occurs in O(1) and is the best case scenario (Omega)
# If we append F to the end of the list, A -> B -> C -> D -> F and that requires iterating through the entire LL to find
# our node to update.  This is the worst case scenario (Omicron, or O(n))
# If we choose to append F to the middle of the list, A -> B -> F -> C -> D, then it would be the average case, but
# would still be considered (O(n)) because we drop consents and go with the closest match.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = 0  # this disconnects the node you are returning from the LL so other nodes cannot be accessed
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        # cnt = 0
        # while cnt < index:
        #     cnt += 1
        #     temp = temp.next
        for _ in range(index):
            temp = temp.next
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
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp_prior = self.get(index - 1)
            temp = temp_prior.next
            temp_prior.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.pop()

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())
my_linked_list.prepend(5)
my_linked_list.prepend(10)
my_linked_list.append(15)
my_linked_list.prepend(12000)
my_linked_list.print_list()
print("*" * 80)
print(my_linked_list.pop_first().value)
print("*" * 80)
my_linked_list.print_list()
print("*" * 80 + "Testing Get")
print(my_linked_list.get(2))
print(my_linked_list.get(4))
print(my_linked_list.get(-1))
my_linked_list.print_list()

print("*" * 80 + "Testing Set")
print(my_linked_list.set_value(2, 25))
print(my_linked_list.set_value(4, 20))
print(my_linked_list.set_value(-1, 400))
my_linked_list.print_list()

print("*" * 80 + "Testing insert")
print(my_linked_list.insert(1, 35))
print(my_linked_list.insert(4, 20))
print(my_linked_list.insert(-1, 400))
my_linked_list.print_list()

print("*" * 80 + "Testing remove")
print(my_linked_list.remove(0))
print(my_linked_list.remove(3))
print(my_linked_list.remove(1))
my_linked_list.print_list()

print("*" * 80 + "Testing reverse")
my_linked_list.print_list()
print(my_linked_list.reverse())
my_linked_list.print_list()
