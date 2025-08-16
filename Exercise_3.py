#Time Complexity : pop : O(N) for all the methods
# Space Complexity : usually all the operations might be in O(1) 
# Did this code successfully run on Leetcode : I ran on a python complier
# Any problem you faced while coding this : No

class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
      
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
       
                  
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        current = self.head
        while current:
            if current.data == key:
                return current.data
            current = current.next

        return None
        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        current = self.head
        previous = None

        while current:
            if current.data == key:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return 
            previous = current
            current = current.next
                






