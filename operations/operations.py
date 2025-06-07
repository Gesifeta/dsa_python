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


    def show_all(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        

my_linked_list = LinkedList(300)
print("Length ",my_linked_list.head.value)
my_linked_list.append(202)
my_linked_list.append(245)
my_linked_list.append(22)
my_linked_list.append(45)
print("*"*100)
my_linked_list.show_all()
print("*"*100)
my_linked_list.show_all()
print("*"*100)
my_linked_list.pop_first()
print("*"*100)
my_linked_list.show_all()
print("*"*100)
my_linked_list.prpend(231)
my_linked_list.prpend(1)
print("Prepended === >")
my_linked_list.show_all()
my_linked_list.get(-7)
my_linked_list.set_value(3,125)
print("Set === >")
my_linked_list.show_all()
print("List === >")
my_linked_list.insert(3,236)
my_linked_list.insert(2,235)
my_linked_list.show_all()
print("Removed === >")
my_linked_list.remove(6)
my_linked_list.show_all()

print("Length ",my_linked_list.length)

        