#!/usr/bin/python3


class Node:
    """Defines a single node of a singly linked list

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None:
            if type(value) != type(self):
                raise TypeError("next_node must be a Node object")
            else:
                self.__next_node = value
        else:
            self.__next_node = None



class SinglyLinkedList:
    """ Defines a singly-linked list of 'Nodes'

    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        my_list = ""
        current = self.__head
        while current.next_node is not None:
            my_list = my_list + str(current.data) + "\n"
            current = current.next_node
        my_list += str(current.data)
        return my_list


    def sorted_insert(self, value):
        newnode = Node(value)

        if self.__head is None:
            self.__head = newnode
        else:
            current = self.__head

            if current.next_node is None:
                if current.data >= value:
                    newnode.next_node = current
                    self.__head = newnode
                else:
                    current.next_node = newnode

            elif (current.next_node.next_node is None):
                if current.data >= value:
                    newnode.next_node = current
                    self.__head = newnode
                elif current.next_node.data >= value:
                    newnode.next_node = current.next_node
                    current.next_node = newnode
                else:
                    current.next_node.next_node = newnode

            else:
                fastnode = self.__head.next_node
                current = self.__head

                if current.data >= value:
                    newnode.next_node = current
                    self.__head = newnode
                    return
                while fastnode is not None:
                    if fastnode.data >= value:
                        newnode.next_node = fastnode
                        current.next_node = newnode
                        return
                    fastnode = fastnode.next_node
                    current = current.next_node

                current.next_node = newnode
