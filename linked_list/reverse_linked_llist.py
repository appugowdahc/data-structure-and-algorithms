class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def insert_node(self,data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            return
        tmp = self.head
        while tmp.next  is not None:
            tmp = tmp.next
            
        tmp.next = node
        
    def reverse_linked_list(self):
        
        if self.head is None:
            print("No nodes available in the list")
            return
        
        prev = None
        curr = self.head
        next_node = None
        
        while curr:
            
            next_node = curr.next
            
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev            
        return prev
    
    def print_linnked_list(self):
        
        if self.head is None:
            print(" No nodes available in list")
            return
        
        node = self.head
        while node:
            print(f"{node.data}-->",end="")
            node = node.next
            
    def delete_node(self,target):
         
        node = self.head
        if target ==1:
            self.head = self.head.next
            return
        prev = self.head
        count = 1
        while node:
            if count == target:
                prev.next = node.next
                return
            prev = node
            node = node.next
            count += 1
        print(" target node is not available")    
        
              
ll = LinkedList()
ll.insert_node(1)
ll.insert_node(2)
ll.insert_node(3)
ll.insert_node(4)
ll.insert_node(5)
ll.insert_node(6)
ll.print_linnked_list()
print("\n")
# ll.reverse_linked_list()
# ll.print_linnked_list()
ll.delete_node(5)
ll.print_linnked_list()

        
        
        
        