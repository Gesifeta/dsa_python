class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail =new_node
            self.length +=1
        else:
            self.tail.next =new_node
            self.tail =new_node
            self.length += 1
    def pop(self):
        if self.head is None:
            return None
        if self.length == 1:
            self.head =None
            self.tail =None
            self.length =0
            return 
        temp = self.head
        prev = self.head
        while(temp.next):
            prev = temp
            temp = temp.next
        self.tail=prev
        self.tail.next =None
        self.length -= 1
            

            
my_linked_list = LinkedList(300)
print("Length ",my_linked_list.head.value)
my_linked_list.append(202)
my_linked_list.append(245)
my_linked_list.append(22)
my_linked_list.append(45)
my_linked_list.pop()
print("Length ",my_linked_list.length)

        