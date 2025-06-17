class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if temp.value == new_node.value:
                return False                        
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right 
       
    def contains(self,value):
        temp = self.root
        while(True):
           
            if temp.value == value:
                return True
            if value > temp.value:
                if temp.right is None:
                    return False
                temp = temp.right
            else:
                if temp.left is None:
                    return False
                temp = temp.left
            



my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(7)
my_tree.insert(67)
my_tree.insert(26)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.root.left.right.value)
print(my_tree.contains(7))