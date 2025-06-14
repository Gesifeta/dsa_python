class Node:
    def __init__(self, value):
        self.value =  value
        self.next = None


class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1


    def show_queue_list(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def enqueue(self,value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
    def dequeue(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp = None
            self.length -= 1
            print(temp)





queue = Queue("Alem")
queue.enqueue("Tigist")
queue.enqueue("Belete")
queue.enqueue("Hagos")
print(f"First = {queue.first.value}")
print(f"Last = {queue.last.value}")
print(queue.show_queue_list())
queue.dequeue()
print(f"First = {queue.first.value}")
print(f"Last = {queue.last.value}")
print(queue.show_queue_list())


