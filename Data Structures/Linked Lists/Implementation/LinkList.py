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
        
    # data adder at start
    def data_adder_front(self,data):
        temp = self.head
        new_node = Node(data)
        self.head = new_node
        self.head.next_node = temp
        
    # Data adder at end
    def none_finder(self,temp,data):
        last_node =None
        if temp.next_node is None:
            temp.next_node = Node(data)
        else:
            self.none_finder(temp.next_node,data)
    
    def data_adder_rare(self,data):
        temp = self.head
        last_node = self.none_finder(temp,data)

    



if __name__=='__main__':
  
    # Start with the empty list
    linked_list = LinkedList()
  
    linked_list.head = Node(1)
    second_node,third_node = Node(2),Node(3)
    
    linked_list.head.next_node = second_node
    second_node.next_node = third_node
    
    linked_list.data_adder_front(5)
    
    linked_list.data_adder_rare(7)
    
    linked_list.All_Elements()