__author__ = 'Clayton'


class Node(object):
    def __init__(self, data):
        self.cargo = data
        self.next = None
        self.previous = None

    def remove(self, data):
        if self.cargo == data:
            self.previous.set_next(self.next)
            if self.next is not None:
                self.next.set_previous(self.previous)
            return 1
        elif self.next is not None:
            return self.next.remove(data)
        else:
            return 0

    def print(self):
        print(self)
        if self.next is not None:
            self.next.print()

    def insert_in_order(self, data):
        if data <= self.cargo:
            new_node = Node(data)
            new_node.set_next(self)
            new_node.set_previous(self.previous)
            self.previous.set_next(new_node)
            self.previous = new_node
        elif self.next is not None:
            self.next.insert_in_order(data)
        else:
            new_node = Node(data)
            new_node.set_previous(self)
            self.set_next(new_node)

    def set_next(self, node):
        self.next = node

    def set_previous(self, node):
        self.previous = node

    def __str__(self):
        return str(self.cargo)


class Sentinel(Node):
    def __init__(self):
        super(Sentinel, self).__init__('Linked List:')
        self.length = 0

    def get_length(self):
        return self.length

    def insert_in_order(self, data):
        if self.next is not None:
            self.next.insert_in_order(data)
        else:
            new_node = Node(data)
            new_node.set_previous(self)
            self.set_next(new_node)
        self.length += 1

    def remove(self, data):
        if self.next is not None:
            self.length -= self.next.remove(data)


class DoublyLinkedList(object):
    def __init__(self):
        self.head = Sentinel()
        self.tail = self.head
        self.ordered = True

    def insert(self, data):
        self.ordered = False
        new_node = Node(data)
        self.tail.next = new_node
        new_node.set_previous(self.tail)
        self.tail = new_node

    def length(self):
        return self.head.get_length()

    def insert_in_order(self, data):
        self.head.insert_in_order(data)

    def remove(self, data):
        self.head.remove(data)

    def print(self):
        print('Length: ' + str(self.length()))
        self.head.print()


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_in_order(1)
    ll.insert_in_order(10)
    ll.insert_in_order(7)
    ll.insert_in_order(11)
    ll.print()
    ll.remove(10)
    ll.print()
    ll.remove(10)
    ll.print()
    ll.remove(1)
    ll.remove(7)
    ll.remove(11)
    ll.print()