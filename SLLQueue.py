from Interfaces import Queue


class SLLQueue(Queue):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        """
        constructor; initializes an empty SLLQueue
        """
        self.head = None
        self.tail = None
        self.n = 0

    def add(self, x: object):
        """
        adds an element to the tail of the queue
        :param x: object type; the new element
        """
        # FIXME: Implement this method
        pass #FIXME: remove

    def remove(self) -> object:
        """
        removes and returns the head of the queue
        :return: object type; the element that was removed from the head of the queue
        :raises: IndexError if the queue is empty
        """
        # FIXME: Implement this method
        pass #FIXME: remove

    def reverse(self):
        """
        reverses the order of the queue
        """
        # FIXME: Implement this method
        pass #FIXME: remove

    def size(self) -> int:
        """
        returns the number of elements in the queue
        :return: int type
        """
        # FIXME: Implement this method
        pass #FIXME: remove

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x