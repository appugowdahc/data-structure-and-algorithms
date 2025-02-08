class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None
        
class linkedList:
    def __init__(self):
        self.head = None
        
    def push_node(self,data):
        node1 = Node(data)
        if self.head is None:
            self.head = node1
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = node1
        return
    def delete_at_begining(self):
        node = self.head
        
        self.head = node.next
        del node
        return
    
    def delete_at_end(self):
        node = self.head
        
        while node.next and node.next.next is not None:
            node = node.next
            
        last_node = node.next
        del last_node
        node.next = None
        return
    def delete_in_middle(self,target):
        
        node = self.head
        count = 1
        while count+1 != target and node.next:
            node = node.next
            count += 1
        target_node = node.next
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None
        del target_node
        return         
        
    def print_ll(self):
        node = self.head
        while node:
            print(str(node.data)+"-->",end ="")  
            node = node.next
        print("\n")
        
        
ll = linkedList()
ll.push_node(1)
ll.push_node(2)
ll.push_node(3)
ll.push_node(4)
ll.push_node(5)
ll.push_node(6)
ll.push_node(7)
ll.push_node(8)
ll.print_ll()
# ll.delete_at_begining()
ll.delete_at_end()
ll.print_ll()


        