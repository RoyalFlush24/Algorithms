class Node(object):
    def __init__(self, id):
        self.id = id
        self.children = []
        
    def __repr__(self):
        return "Node: [%s]" % self.id
    
    def add_child(self, node):
        self.children.append(node) 
    
    def get_children(self):
        return self.children         
    
    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children     
      
a0 = Node("a0")
b0 = Node("b0")      
b1 = Node("b1")      
b2 = Node("b2")      
c0 = Node("c0")      
c1 = Node("c1")  
d0 = Node("d0")   
    
a0.add_child(b0) 
a0.add_child(b1) 
a0.add_child(b2)
    
b0.add_child(c0) 
b0.add_child(c1)

print a0.get_rev_children()
print a0.get_children()
print a0.__repr__()
