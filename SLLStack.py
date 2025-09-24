from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        """
        constructor; initializes an empty stack
        """
        # FIXME: Implement this method
        pass #FIXME: remove

    def push(self, x: object):
        """
        adds a new element to the head of the stack
        :param x: object type; the new element
        """
        # FIXME: Implement this method
        pass #FIXME: remove

    def pop(self) -> object:
        """
        removes and returns the element at the head of the stack
        :return: object type; the element that was removed from the stack
        :raises: IndexError if the stack is empty
        """
        # FIXME: Implement this method
        pass #FIXME: remove

    def size(self) -> int:
        """
        returns the number of elements in the stack
        :return: int type;
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




