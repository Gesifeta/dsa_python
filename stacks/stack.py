class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1


    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node        
        else:
             new_node.next = self.top
             self.top = new_node
        self.height += 1
    

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1

    def show_stack_list(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next





stack = Stack(4)
stack.push(6)
stack.push(8)
stack.push(12)
stack.push(6)
stack.push(8)
stack.push(12)
stack.pop()
print(stack.show_stack_list())
