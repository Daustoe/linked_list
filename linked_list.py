__author__ = 'Clayton'


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, node):
        self.next = node

    def remove(self, data):
        if self.next is not None:
            if self.next.data == data:
                self.next = self.next.next
            else:
                self.next.remove(data)

    def print(self):
        print(self)
        if self.next is not None:
            self.next.print()

    def __str__(self):
        return str(self.data)


class Sentinel(Node):
    def __init__(self):
        super(Sentinel, self).__init__('Sentinel, Error')

    def print(self):
        if next is not None:
            self.next.print()


class SimpleLinkedList(object):
    def __init__(self):
        self.head = Sentinel()
        self.tail = self.head

    def insert(self, data):
        new_node = Node(data)
        self.tail.set_next(new_node)
        self.tail = new_node

    def remove(self, data):
        self.head.remove(data)

    def print(self):
        self.head.print()


if __name__ == '__main__':
    ll = SimpleLinkedList()
    ll.insert(1)
    ll.insert(12)
    ll.insert(5)
    ll.print()
    ll.remove(5)
    ll.print()
    ll.remove(1)
    ll.print()