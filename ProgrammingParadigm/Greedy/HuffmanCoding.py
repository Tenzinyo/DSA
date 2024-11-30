# def huffmanCoding(c):
#   n=len(c)
#   Q=c
#   for i in len(1,n-1):
#     temp=
#code reference from Geek
import heapq
class node:
  def _init_(self,freq,left=None,right,None,symbol):
    self.freq = freq
    self.symbol
    self.left=left
    self.right=right
    self.huffman=''
  def _lt_(self,next):
    return self.freq<next.freq
    
def nodesOutput(node, value=''): 
    newValue= val + str(node.huffman) 
    if(node.left): 
      # next= newValue
      nodesOutput(node.left, newValue) 
    if(node.right): 
      nodesOutput(node.right, newValue) 
    if(not node.left and not node.right): 
      print(f"{node.symbol} -> {newVal}") 
  
chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
freq = [5, 9, 12, 13, 16, 45] 
nodes = []
