class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
    

    def isEmpty(self):
        return len(self.items) == 0
      

    def push(self, items):
       if len(self.items) < self.limit:
         self.items.append(items)
    

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
     

    def peek(self):
        if not self.isEmpty:
            return self.items[-1]
        
       
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit
        

    def search(self, target):
        try:
            index =self.items.index(target)
            return len(self.items) - index -1
        except ValueError:
            return -1
        
