# 2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих
# циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.


class ListFifo:

    def __init__(self, size):
        self.__size = size

        self.queue = [None] * size

        self.__head = -1
        self.__tail = -1

    def equeue(self, element):

        if (self.__tail + 1) % self.__size == self.__head:
            raise Exception("Queue is full. Can't add a new element")

        elif self.__head == -1:
            self.__head += 1

        elif self.__head == self.__size:
            self.__head = 0

        self.__tail = (self.__tail + 1) % self.__size
        self.queue[self.__tail] = element

    def dequeue(self):
        if self.__head == -1:
            raise Exception("Queue is empty")

        result = self.queue[self.__head]
        self.queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__size

        if self.count() == 0:
            self.__head = -1
            self.__tail = -1

        return result

    def count(self):
        result = 0
        for elem in self.queue:
            if elem is not None:
                result += 1
        return result

    def peek(self):
        return self.queue[self.__head]


a = ListFifo(4)
b = ListFifo(4)
print(a == b)