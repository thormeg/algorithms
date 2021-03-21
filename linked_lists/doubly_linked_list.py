"""Doubly Linked List."""

class Node:
    """Single node class."""
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def __repr__(self):
        if (self.head == None):
            return 'List is currently empty.'
        
        contents = f'Contents of linked list:\n{self.head.data}'
        node = self.head.next
        while (node != None):
            contents += f' > {node.data}'
            node = node.next
        return contents

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.count = 1
            return
        
        self.tail.next = Node(data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.count += 1

    def insert(self, data, index):
        if (index < 0) or (index > self.count):
            print(f'Index {index} out of bounds')
            return

        if index == self.count:
            self.append(data)
            return

        if index == 0:
            self.head.previous = Node(data)
            self.head.previous.next = self.head
            self.head = self.head.previous
            self.count += 1
            return

        node = self.head
        for _ in range(index):
            node = node.next
        node.previous.next = Node(data)
        node.previous.next.previous = node.previous
        node.previous.next.next = node
        node.previous = node.previous.next
        self.count += 1        

    def remove(self, index):
        if (index >= self.count) or (index < 0):
            print('Requested remove index out of bounds. Please choose another')
            return
        
        if index == 0:
            if self.head == self.tail:
                self.tail = None
                self.head = None
                self.count -= 1
                return

            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
            return
        
        if index == (self.count - 1):
            self.tail = self.tail.previous
            self.tail.next = None
            self.count -= 1
            return

        node = self.head
        for _ in range(index):
            node = node.next
        node.previous.next = node.next
        node.next.previous = node.previous
        self.count -= 1
        return
    
    def get(self, index):
        if (index < 0) or (index > (self.count + 1)):
            print(f'Index {index} out of bounds.')
            return

        node = self.head
        for i in range(self.count):
            if i == index:
                return node

            node = self.head.next

    def show(self):
        print(self)

    def size(self):
        print(self.count)

if __name__ == '__main__':
    l = DoublyLinkedList()
    l.append(1)
    l.append(2)
    l.append(3)