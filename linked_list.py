__author__ = 'Clayton'


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, node):
        self.next = node

    def __str__(self):
        return str(self.data)


class Linkedlist(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def print(self):
        node = self.head
        while node:
            print(node)
            node = node.next


if __name__ == '__main__':
    ll = Linkedlist()
    ll.add(1)
    ll.add(12)
    ll.add(5)
    ll.print()