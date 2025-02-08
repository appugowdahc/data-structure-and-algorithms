class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def find_length(self):
        curr_node = self.head
        length = 0
        while curr_node is not None:
            length += 1
            curr_node = curr_node.next
        return length
    
    def insert_at_head(self,node):
        node.next = self.head
        self.head = node
        return
    
    def insert_at_position(self,node,position):
        if position is 0:
            self.insert_at_head(node)
            return
        if position < 0 or position > self.find_length():
            print("invalid position")
            return
        curr_node = self.head
        prev_node = None
        curr_position = 0
        while True:
            if position == curr_position:
                prev_node.next = node
                node.next = curr_node
                break
            prev_node = curr_node
            curr_node = curr_node.next 
            curr_position += 1   
        return
    
    def insert(self,new_node):
        
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next!=None:
                curr_node = curr_node.next
            curr_node.next = new_node
    def printList(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            curr_node = self.head
            while curr_node:
                print(curr_node.data)
                curr_node = curr_node.next
                
        return
                
            
appu = Node("appu")
pavitra = Node("pavitra")
gagana = Node("gagana")
gowda =Node("gowda")
place = Node("mandya")
 
llist = LinkedList()
llist.insert(appu)
llist.insert(pavitra)
llist.insert(gagana)
llist.insert_at_head(gowda)
llist.insert_at_position(place,3)
llist.printList()
