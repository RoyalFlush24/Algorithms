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
     

class LinkedList:
  def __init__(self,head=None):
    self.head=head;
    
    
  def insert(self,item):
    new_node=Node(item)  # make a new node having data=item and points to NULL
    new_node.set_next(self.head) # set the pointer of new node
    self.head=new_node  #make a new node as head
  
  def size(self):
    current=self.head # set head node as current
    count=0  # take a count varaible for counting the nodes
    while current:
      count +=1 # increment the counter value
      current=current.get_nextnode() # set to current node 
      
    return count
    
  def search(self,item):
    current=self.head
    found=False
    while current and found is False:
      if(current.get_data() == item):
        found=True
      else:
        current=current.get_nextnode()
        
    return found
        
  def delete(self,item):
    current=self.head
    previous=None
    found=False
    while found is False:
      if(current.get_data() == item):
        found=True
      else:
        previous=current
        current=current.get_nextnode()
       
    if previous == None:
      self.head=current.get_nextnode()
    else:
      previous.set_next(current.get_nextnode())
      
       
    
# make a LinkedList
newlist=LinkedList()

# inserting item in LinkedList
newlist.insert(11)
newlist.insert(23)
newlist.insert(67)
newlist.insert(87)

# check the size of list
print newlist.size()

# search the item in the list
print newlist.search(11)
  
# delete item

newlist.delete(23)

# check the size again after deleting the item in  list
print newlist.size()
