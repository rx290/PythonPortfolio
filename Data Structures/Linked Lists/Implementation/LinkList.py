# Implementation of Link List

class Node:
# instance attributes
 def __init__(self, data=None):
   # Data initialization and assignment
   self.data = data
   # Next node Reference set as null
   self.next_node = None

# instance method
class LinkedList:
    def __init__(self):
      self.head = None
    
    def node_printer(self,temp):
        if temp.next_node is not None:
            print(temp.data)
            self.node_printer(temp.next_node)
        else:
            print(temp.data)
    
    # Method to print all elements
    # starting from head
    def All_Elements(self):
        temp = self.head
        self.node_printer(temp)
    



if __name__=='__main__':
  
    # Start with the empty list
    linked_list = LinkedList()
  
    linked_list.head = Node(1)
    second_node,third_node = Node(2),Node(3)
    
    linked_list.head.next_node = second_node
    second_node.next_node = third_node
    
    linked_list.All_Elements()