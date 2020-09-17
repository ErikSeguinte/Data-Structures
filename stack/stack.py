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
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.size = 0

        self.array = [None] * self.capacity

    def append(self, element):
        if self.size == self.capacity:
            self.grow()
        self.array[self.size] = element
        self.size += 1

    def get_element(self, position:int):
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

        for i,e in enumerate(self.array[:self.size]):
            new_array[i] = e

        self.array = new_array

    def print(self):
        print(self.array[:self.size])


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

class Stack(ArrayStack):
    pass
