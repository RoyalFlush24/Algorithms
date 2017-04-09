class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s = Stack()
s.push('one')
s.push('two')
s.push('three')
print s.size()
print s.peek()
print(s.pop())
print s.peek()
print s.isEmpty()
