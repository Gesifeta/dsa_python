class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
           self.head = new_node
           self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev= self.tail
            self.tail = new_node
            self.length += 1
        return True
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.tail
            self.tail= self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
        return True
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next=self.head
            self.head.prev= new_node
            self.head = new_node
            new_node.prev= None
            self.length += 1
        return True
    def pop_first(self):
        # check if the list exist
        if self.length == 0:
            return None
        if self.length == 1:
           self.head = None
           self.tail = None
           self.length -= 1
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -= 1
        
    def showList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
doubly_linked_list = DoublyLinkedList(2)
doubly_linked_list.append(26)
doubly_linked_list.append(6)
print(doubly_linked_list.showList())
doubly_linked_list.pop()
print(doubly_linked_list.showList())
doubly_linked_list.prepend(23)
doubly_linked_list.prepend(22)
doubly_linked_list.prepend(4)
doubly_linked_list.prepend(25)
print(doubly_linked_list.showList())
doubly_linked_list.pop_first()
doubly_linked_list.pop_first()
print(doubly_linked_list.showList())
