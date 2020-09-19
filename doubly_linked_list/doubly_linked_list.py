"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head:ListNode = node
        self.tail:ListNode = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        node = ListNode(value, next=self.head)

        if self.head:
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node

        self.length +=1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        head = self.head
        if len(self) == 1:
            self.tail = None
            self.head = None
            self.length -=1
        elif self.head:
            nxt = self.head.next
            self.head = nxt
            self.head.prev = None
            self.length -= 1

        return head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        node = ListNode(value, prev=self.tail)

        # if there is no tail, then this method is equivilent to add to head
        if not self.tail:
            self.add_to_head(value)
            return
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        tail = self.tail
        if self.length == 1:
            self.remove_from_head()
        elif self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

        return tail.value



    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        v = self.delete(node)
        self.add_to_head(v)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        v = self.delete(node)
        self.add_to_tail(v)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head == node and self.tail == node:
            self.tail = None
            self.head = None
        else:
            p = node.prev
            n = node.next

            if p:
                p.next = n
            else:
                self.head = n
            if n:
                n.prev = p
            else:
                self.tail = p

        self.length -= 1

        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        max_value = self.head.value

        node = self.head.next
        while node:
            if node.value > max_value:
                max_value = node.value

            node = node.next

        return max_value


if __name__ == "__main__":
    node = ListNode(1)
    dll = DoublyLinkedList(node)

    dll.delete(node)
    dll.add_to_tail(1)
    dll.add_to_head(9)
    dll.add_to_tail(6)
    dll.delete(dll.head.next)
    dll.delete(dll.head)
    assert(dll.head == dll.tail)