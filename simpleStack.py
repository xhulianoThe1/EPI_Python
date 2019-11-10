class Stack(): 
  def __init__(self): 
    self.items = []
  def push(self,item): 
    self.items.append(item)

  def pop(self): 
    return self.items.pop()

  def getStack(self): 
    return self.items

s = Stack() 
s.push(1)
s.push(2)
s.push(3)
print(s.getStack())
s.pop()
s.pop()
print(s.getStack())
