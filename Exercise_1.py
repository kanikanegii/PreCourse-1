class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file


# Time Complexity : pop : O(1) for all the methods
# Space Complexity : O(N) where N is the length of stack 
# Did this code successfully run on Leetcode : I ran on a python complier
# Any problem you faced while coding this : No

  def __init__(self):
      self.arr = []
      
  def isEmpty(self):
    if not self.arr:
      return True
    else:
      return False
      
  def push(self, item):
    return self.arr.append(item)
      
  def pop(self):
    if not self.arr:
      return -1
    return self.arr.pop()
    
  def peek(self):
    return self.arr[-1]
    
  def size(self):
    return len(self.arr)
      
  def show(self):
    return self.arr
      

if __name__ == "__main__":
  s = myStack()
  s.push('1')
  s.push('2')
  print(s.pop())  #O(1)
  print(s.show())
