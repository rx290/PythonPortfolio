"Write a Python program to delete the last item from a singly linked list." 
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next_node = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def Transversal(self,temp):
        if temp.next_node is not None:
            print(temp.data)
            self.Transversal(temp.next_node)
        else:
            print(temp.data)
            
    def Element_Printer(self):
        temp = self.head
        self.Transversal(temp)
        
    
    
    
    
linkedlist = LinkedList()

node_1 , node_2, node_3 = Node(1),Node(3),Node(6)

linkedlist.head = node_1

node_1.next_node=node_2
node_2.next_node= node_3

print(linkedlist.Element_Printer())