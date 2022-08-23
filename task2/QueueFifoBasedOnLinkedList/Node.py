class Node:

    def __init__(self, data, next):
        self.__data = data
        self.__next = None
        self.set_next(next)

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, next):
        if type(next) is not Node and next is not None:
            raise TypeError(f'`next` expected type is None or Node, but actual type is {type(next)}')
        self.__next = next
