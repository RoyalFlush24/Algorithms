class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)	     
q=Queue()
q.enqueue('udacity')
q.enqueue('anum')
q.enqueue(True)
q.enqueue(2017)
print(q.isEmpty())
print(q.size())
q.dequeue()
print q.size()
