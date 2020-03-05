" Getting all the values at a certain height in a binary tree "
class Node(): 
  #initialization func
  def __init__(self, value, left = None, right = None): 
    self.value = value
    self.left = left
    self.right = right
  
def valsAtHeight(node, depth) : 
  #base cases 
  if node is None: 
    return []
  #Return value of the node
  if depth == 1:
    return [node.value] 
  #recursion 
  return valsAtHeight(node.left, depth - 1) + valsAtHeight(node.right, depth-1)

# " Driver function"
#    1
#   / \
#  2   3
# / \   \
# 4   5   7
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.right.right = Node(7)
node.left.left = Node(4)
node.left.right = Node(5)
#print the values at all 3 heights 
print(valsAtHeight(node, 1))
print(valsAtHeight(node, 2))
print(valsAtHeight(node, 3))

