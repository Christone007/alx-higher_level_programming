#!/usr/bin/python3

"""This module creates a singly-linked list
in python code using Classes
"""


class Node:
    """Defines a Node"""

    def __init__(self, data, next_node=None):
        """Initializes a Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly-linked list of Nodes"""

    def __init__(self):
        self.__head = []

    def __str__(self):
        result = ""
        for i in self.__head:
            result += str(i.data)
            if (self.__head.index(i) < len(self.__head) - 1):
                result += "\n"
        return (result)

    def sorted_insert(self, value):
        """inserts a new node and sorts the list"""
        new_node = Node(value)

        self.__head.append(new_node)
        self.__head = sorted(self.__head, key=lambda x: x.data, reverse=False)
