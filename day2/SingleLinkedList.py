class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

        
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head= new_node
        self.tail = new_node
        self.length = 1
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail=new_node
            self.length += 1
    def print_all_nodes(self):
        temp =self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

         
my_linked_list = LinkedList(4)
my_linked_list.append(56)
my_linked_list.append(58)
my_linked_list.append(4)
my_linked_list.append(104)
print((my_linked_list.length))
print((my_linked_list.print_all_nodes()))
