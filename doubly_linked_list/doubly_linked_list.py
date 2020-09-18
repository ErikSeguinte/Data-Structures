"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


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
    def __init__(self, head=None):
        if head is not None:
            node = head
            self.size = 1
        else:
            node = None
            self.size = 0
        self.tail = node
        self.head = node

    def insertleft(self, data):
        new_head = ListNode(data, self.head)
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

    def insert_right(self, data):

        # if empty, inserting right is equivalent to inserting the left.
        if self.tail is None:
            self.insertleft(data)
        else:
            new_tail = ListNode(data, prev=self.tail)
            self.tail.next_node = new_tail
            self.tail = new_tail

    def pop_right(self):
        node = self.tail

        if node:
            prev = node.prev_node

            # Additional list remains. Next node is now the new head.
            if prev:
                prev.next_node = None
                self.tail = prev

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


class ListNode(Node):
    def __init__(self, value, prev=None, next=None):
        super().__init__(value, next, prev)
        self.value = self.data

    @property
    def value(self):
        return self.data

    @value.setter
    def value(self, new_value):
        self.data = new_value

    @property
    def next(self):
        return self.prev_node

    @property
    def prev(self):
        return self.next_node

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList(LinkedList):
    def __init__(self, node=None):
        super().__init__(node)

    def __len__(self):
        return self.size
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.insertleft(value)
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        self.popleft()

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.insert_right(value)
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.pop_right()
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def remove_and_reconnect(self, node:ListNode):
        prev = node.prev_node
        nxt = node.next_node

        if prev:
            prev.next_node = nxt
        if nxt:
            nxt.prev_node = prev

    def move_to_front(self, node:ListNode):
        self.remove_and_reconnect(node)
        self.insertleft(node.data)
        del node


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.remove_and_reconnect(node)
        self.insert_right(node.data)
        del node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.remove_and_reconnect(node)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            raise IndexError

        max_value = self.head.value
        node = self.head.next_node
        while node:
            if node.value > max_value:
                max_value=node.value
            node = node.next_node
        return max_value