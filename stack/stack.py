"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0

        self.array = [None] * self.capacity

    def append(self, element):
        if self.size == self.capacity:
            self.grow()
        self.array[self.size] = element
        self.size += 1

    def get_element(self, position: int):
        if position < 0 or position > self.size:
            raise IndexError
        else:
            return self.array[position]

    def pop(self):
        if self.size <= 0:
            return None

        value = self.get_element(self.size - 1)

        if self.size <= self.capacity // 4:
            self.shrink()

        self.size -= 1
        return value

    def grow(self):
        old_capacity, self.capacity = self.capacity, self.capacity * 2

        new_array = [None] * self.capacity

        for i, e in enumerate(self.array):
            new_array[i] = e

        self.array = new_array

    def shrink(self):
        if self.capacity == 1:
            return
        self.capacity = self.capacity // 2
        new_array = [None] * self.capacity

        for i, e in enumerate(self.array[: self.size]):
            new_array[i] = e

        self.array = new_array

    def print(self):
        print(self.array[: self.size])


class ArrayStack(DynamicArray):
    def __init__(self):
        super().__init__()
        self.size = 0
        # self.storage = ?

    def __len__(self):
        return self.size

    def push(self, value):
        self.append(value)

    def pop(self):
        try:
            return super().pop()
        except IndexError:
            return None


# class Stack(ArrayStack):
#     pass


class Node:
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


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.size = 0
        self.head = head
        self.tail = tail

    def insertleft(self, data):
        new_head = Node(data, self.head)
        if self.head:
            self.head.prev_node = new_head
        else:
            self.tail = new_head
        self.head = new_head
        self.size += 1

    def popleft(self):
        node = self.head

        if node:
            nxt = node.next_node

            # Additional list remains. Next node is now the new head.
            if nxt:
                nxt.prev_node = None
                self.head = nxt

            # empty list. Reset tail and head to None
            else:
                self.head = None
                self.tail = None

            self.size -= 1
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


class ListStack(LinkedList):
    def __init__(self):
        super().__init__()

    def __len__(self):
        return self.size

    def push(self, value):
        self.insertleft(value)

    def pop(self):
        return self.popleft()


class Stack(ListStack):
    pass
