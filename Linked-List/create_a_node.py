# make a node that contain data and pointer
class Node: 
  def __init__(self,data=None,next_node=None):
    self.data=data
    self.next_node=next_node
    
  def get_data(self):
    return self.data # fetching the data from the node
  
  def get_nextnode(self):
    return self.next_node    #know about the next node 
    
  def set_next(self,new_node):
    self.next_node=new_node
     

# testing the Node 

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
print node1.get_data()
print node3.get_nextnode().get_data()


"""
output:
10
40

   (node4)--> (node3) --> (node2)   -->  (node1)
       (40)   -->  (30)       -->(20)          -->(10)
"""
