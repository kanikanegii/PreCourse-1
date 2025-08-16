

# Time Complexity : pop : O(1) for all the methods
# Space Complexity : usually all the operations might be in O(1) but worst case scenario O(N) where N is the length of stack 
# Did this code successfully run on Leetcode : I ran on a python complier
# Any problem you faced while coding this : No



class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None

     #Approach used is to add new data at the start of the head    
    def push(self, data):

        new_node= Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):

        if self.head:
            remove = self.head.data
            self.head = self.head.next
            return remove
        else:
            return None

if __name__ == "__main__":   

    a_stack = Stack()
    while True:
        #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
        print('push <value>')
        print('pop')
        print('quit')
        do = input('What would you like to do? ').split()
        #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
        operation = do[0].strip().lower()
        if operation == 'push':
            a_stack.push(int(do[1]))
        elif operation == 'pop':
            popped = a_stack.pop()
            if popped is None:
                print('Stack is empty.')
            else:
                print('Popped value: ', int(popped))
        elif operation == 'quit':
            break
