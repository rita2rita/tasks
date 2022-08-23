from LinkedList import LinkedList


class QueueFifo(LinkedList):

    def __init__(self, max_size):
        self.max_size = max_size

    def equeue(self, element):
        current_size = self.count()
        if current_size == self.max_size:
            raise Exception("Queue is full. Can't add element")
        else:
            LinkedList.add_last(self, element)

    def dequeue(self):
        returned_element = self.get(0)
        LinkedList.remove(self, 0)
        return returned_element

    def peek(self):
        current_size = self.count()
        LinkedList.get(self, current_size - 1)
