#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        """We instantiate the new node object, with no data in it, and no pointer
           to the next node ( could change )"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

# Our LinkedList class takes an object
class LinkedList(object):
    """in iterable is an object with a next method, if
    we do object.next it'll cause us to do iteration"""
    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        # This instantiates the empty linked list, no head, no tail
        self.head = None
        self.tail = None
        # (like feeding in a list )if it receives a list, return that object, then return the next one
        if iterable:
            # iterate through the iterable
            for item in iterable:
                # grab the current object it's iterating through and add it to our linkedList
                self.append(item)
                #Now our linked list class contains objects


    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        ''' In this method we sort of convert into a list '''
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    # self is the LinkedList here, we're checking if the linked list is empty
    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        # if there is no node in the list, it's emtpy

        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # at first, we set the count to zero
        count = 0
        # we set our current node (start) to be the head of the linked list
        current_node = self.head
        # if the current node hasn't reached the end of the linked list keep iterating
        while current_node is not None:
            # currrent node is not the last one, so increase the count by 1
            count += 1
            # then set the new current node to the next node. This allows us to keep iterating. Next to next to next to next
            current_node = current_node.next
        # then we return the count
        return count


# lets append a new item to the linked list
    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        """
        If the linked list is empty, add a node to it.
        Then set it as the head and the tail ( so that we could add to it ( if we have a tail, it's also adding a reference to it))
        """
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        elif self.head == self.tail:
            # if it's the tail, add a new node to it
            self.tail = Node(item)
            self.head.next = self.tail
        else:
            new_tail = Node(item)
            self.tail.next = new_tail
            self.tail = new_tail

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # TODO: prepend given item
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        elif self.head == self.tail:
            self.head = Node(item)
            self.head.next = self.tail
        else:
            new_head = Node(item)
            new_head.next = self.head
            self.head = new_head


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        last_node = None
        current = self.head
        while current is not None: # Up to n iterations, so worst case 0(n)
            if current.data == item:
                if last_node:
                    last_node.next = current.next
                if self.head == current:
                    self.head = current.next
                if self.tail == current:
                    self.tail = last_node
                current_node = None
                return
                last_node = current
            current = current.next
        raise ValueError


    def find(self, quality):
        current_node = self.head # Constant time to assign a variable reference
        while current_node is not None: # Up to n iterations, so worst case O(n)
            if quality(current_node.data):  # Constant time to call quality(data)
                return current_node.data # Constant time to return data early
            current_node = current_node.next # Constant time to skip to the next node

def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
