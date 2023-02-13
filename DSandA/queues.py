#  Queue is different from stack.  In stack, we continue to pile objects on each other, however with the queue, we
#  have a first and last, and only add to the back.  When we add someone to the queue the go to the end of the current
#  queue similar to a line at a roller coaster.  This is called FIFO, or first in first out.

#  The reason for this is that efficiency dictates that it is quicker to remove someone to the front in O(1) and adding
#  from the end is O(1).  We call removing an object dequeuing and adding an object enqueuing


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.prev
        while temp:
            print(temp.value)
            temp = temp.prev

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
