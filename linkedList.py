class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element



# Test cases
# Set up some Elements
e1 = Element("anum")
e2 = Element("sharma")
e3 = Element("udacity")
e4 = Element("nanodegree")

# Start setting up a LinkedList
print "appending element in head node(e1):-"
ll = LinkedList(e1)
print "appending elements in node(e2, e3):-"
ll.append(e2)
ll.append(e3)

# Test get_position
print "get head next value:-"
print ll.head.next.value
print "get the value on specific position(3):-"
print ll.get_position(3).value

# Test insert
print "****INSERTING e4 ON 3RD POSITION****"
ll.insert(e4,3)

print "get value on specific position(1):-"
print ll.get_position(1).value
