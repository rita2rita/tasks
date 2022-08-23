from Node import Node


class LinkedList:
    """
    We consider the "Linked List" as a sequence of elements from left to right.
    The most left element has index [0], the most right element has [size-1]
    The element with index [0] is "the first element", the element with index [size-1] is "the last element"
    """
    __root = None

    def add(self, index, data):
        node = Node(data, None)
        node.set_next(None)
        size = self.count()
        index_of_left_node = index - 1

        if index == 0:  # add first
            right_node = self.__root
            self.__root = node
            node.set_next(right_node)

        elif size == 0 and index > 0 or size != 0 and index > size:
            raise IndexError(f'Node index out of queue, current queue size is {size}')

        else:
            left_node = self._get_node(index_of_left_node)
            right_node = left_node.get_next()
            left_node.set_next(node)
            node.set_next(right_node)

    def add_last(self, data):
        size = self.count()
        node = Node(data, None)
        node.set_next(None)

        if size > 0:
            last_node = self._get_node(size - 1)
            last_node.set_next(node)
        else:
            self.__root = node

    def add_first(self, data):
        node = Node(data, None)
        node.set_next(None)

        right_node = self.__root
        self.__root = node
        node.set_next(right_node)

    def get(self, index):
        size = self.count()
        max_index = size - 1
        if index > max_index:
            raise IndexError('Node index out of queue')
        else:
            node = self.__root
            for i in range(index + 1):
                if i == index:
                    return node.get_data()
                node = node.get_next()

        return node.get_data()

    def remove(self, index):
        deleted_node = self._get_node(index)
        size = self.count()

        if size == 0:
            raise Exception('Queue is empty')

        elif size == 1:
            if index == 0:
                self.__root = None
            else:
                raise IndexError(f'Node index out of queue, current queue size is {size}')
        else:
            if index == 0:
                self.__root = deleted_node.get_next()
            elif index == size - 1:
                self._get_node(index - 1).set_next(None)
            else:
                if index < size - 1:
                    left_node = self._get_node(index - 1)
                    right_node = self._get_node(index + 1)
                    left_node.set_next(right_node)

    def count(self):
        counter = 0
        node = self.__root

        while type(node) == Node:
            counter += 1
            node = node.get_next()

        return counter

    def _get_node(self, index):
        size = self.count()
        max_index = size - 1
        if index > max_index:
            raise IndexError('Node index out of queue')
        else:
            node = self.__root
            for i in range(index + 1):
                if i == index:
                    return node
                node = node.get_next()

        return node
