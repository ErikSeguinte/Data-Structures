"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from collections import deque


class ArrayQueue:
    def __init__(self):
        self.size = 0
        self.array = deque()

    def __len__(self):
        return len(self.array)

    def enqueue(self, value):
        self.array.appendleft(value)

    def dequeue(self):
        if len(self.array) == 0:
            return None
        return self.array.pop()


class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def print_node(self):
        if self.data:
            print(
                "self",
                self.data,
                ", next:",
                self.next_node.data,
                ", prev:",
                self.prev_node.data,
            )
        else:
            print("Empty Node")


class linked_list:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def insertleft(self, data):
        new_head = Node(data, self.head)
        if self.head:
            self.head.prev_node = new_head
        else:
            self.tail = new_head
        self.head = new_head
        self.size += 1

    def popright(self):
        self.size -= 1
        node = self.tail

        if node:
            prev = node.prev_node

            # Additional list remains. Next node is now the new tail
            if prev:
                prev.next_node = None
                self.tail = prev

            # empty list. Reset tail and head to None
            else:
                self.head = None
                self.tail = None

            return node.data

        else:
            return None

    def search(self, data):
        current = self.head
        found = False

        while current and not found:
            if current.data == data:
                found = True
            else:
                current = current.next_node
        if current:
            return current
        else:
            return None

    def print_node(self, data):
        node = self.search(data)

        if node:
            node.print_node()
        else:
            print("Node does not Exist")

    def remove(self, data):
        node = self.search(data)

        # Node not found.
        if not node:
            return
        prev = node.prev_node
        nxt = node.next_node

        # Node is a middle link with a previous and next
        if prev and nxt:
            prev.next_node = nxt
            nxt.prev_node = prev

        #  Node is tail node. No next node.
        elif prev and not nxt:
            prev.next_node = None
            self.tail = node.prev_node

        #  Node is head node. No previous node.
        elif nxt and not prev:
            nxt.prev_node = None
            self.head = node.next_node

        #  Node is both head and tail, leaving empty list.
        else:
            self.head = None
            self.tail = None

        return

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_node


class ListQueue(linked_list):
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.insertleft(value)

    def dequeue(self):
        if self.size == 0:
            return None
        return self.popright()

from stack.stack import Stack

class StackQueue(linked_list):

    def __init__(self):
        super().__init__()
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.__len__ == 0:
            return None
        if len(self.stack2) > 0:
            return self.stack2.pop()

        else:
            while len(self.stack1) > 0:
                self.stack2.push(self.stack1.pop())

            return self.stack2.pop()


class Queue(StackQueue):
    pass
