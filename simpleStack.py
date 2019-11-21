class Stack(): 
  def __init__(self): 
    self.items = []
  #Add items to the stack 
  def push(self,x): 
    self.items.append(x)
  #Pop items from the stack 
  def pop(self): 
    return self.items.pop()
  #If the stack is empty 
  def isEmpty(self): 
    return self.items() == []
  #Return items from the stack 
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
