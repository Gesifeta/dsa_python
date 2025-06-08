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
    def prpend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head= new_node
            self.tail =new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.next= temp

    def pop_first(self):
        if self.length == 0:
            return None
        self.head = self.head.next
        self.length -= 1

    def get(self, index):
        if self.length < index or index<0:
            return False
        if self.length == 1:
            self.head.value
            return True
        else:
            temp = self.head
            for _ in range(1, index):
                temp = temp.next  
            print(f"The value at the index is {index} is {temp.value}")
            return True
    def set_value(self,index,value):
         if self.length < index or index < 0:
            return print("Not in a range")
         if self.length == 1:
            self.head.value = value
         else:
             temp = self.head
             for _ in range(1, index):
                 temp = temp.next
             temp.value =value
    def insert(self,index,value):
        print(self.get(index))
        if self.get(index):
            new_node = Node(value)
            if self.length == 1:
                self.head = new_node
                self.tail = new_node
                self.length += 1
            elif self.length == index:
                self.tail = new_node
                self.tail.next = None
                self.length += 1
            else:
                temp = self.head
                prev = self.head
                for _ in range(1, index):
                    prev = temp
                    temp =temp.next
                prev.next = new_node
                new_node.next= temp
                self.length += 1
        else:
            return self.get(value)
    def remove(self,index):
        if self.get(index):
            prev = self.head
            temp = self.head
            if self.length == 0:
                return None
            if self.length == 1:
                self.head = None
                self.tail = None
                self.length -= 1
            for _ in range(1, index):
                prev = temp
                temp = temp.next
            prev.next = temp.next
            self.length -= 1
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        next = temp.next
        prev = None
        for _ in range(self.length):
           next = temp.next
           temp.next = prev
           prev= temp
           temp = next
           
    def show_all(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.insert(4,1)
print("*"*100)
print("List === >")
my_linked_list.show_all()
my_linked_list.reverse()
print("Reversed === >")
my_linked_list.show_all()


        