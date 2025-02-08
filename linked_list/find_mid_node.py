class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push_to_list(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        tmp = self.head 
        while tmp.next:
            tmp = tmp.next
        tmp.next = node
        return
               
    def printList(self):
        print("\n")
        node = self.head
        while node:
            print(f"-->{node.data}",end=" ")
            node = node.next
        print("\n")
    def find_len(self):
        if self.head is None:
            return 0
        node = self.head
        store = []
        while node.next:
            store.append(node.data)
            node = node.next
        store.append(node.data)
        return (len(store),store)
    
    #to find mid element by using array and length and time ,space is O(n),O(n)
    def find_mid_ele(self):
        l,values = self.find_len()
        print(f"The mid node of linked list is {values[l//2]}")
        
    #to find mid element by using array and length and time ,space is O(2*n)==> O(N),O(1)
    def find_mid_by_count(self):
        if self.head is None:
            print("There is no node available")
            return
        node = self.head
        count = 1
        while node.next:
            node = node.next
            count += 1
        node = self.head
        count = count//2
        while count:
            node=node.next
            count -= 1
        print(f"The mid node of linked list is {node.data}")
        return
    
    # using Floyd's cycle finding algorithm or hare and tortoise algorithm
    def find_mid_by_floyds_cycle(self):
        
        if self.head is None:
            print("No node available")
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        print(f"The mid node of linked list is {slow.data}")
        return 
        
        
    #Find Middle of the Linked List by Counting Nodes (One-pass):
    def find_mid_by_counter(self):
        mid = self.head
        counter = 1
        head = self.head
        while head:
            if counter % 2 == 0:
                mid = mid.next
            head = head.next
            counter += 1
            
        print(f"The mid node of linked list is {mid.data}")
        return
        
    
ll = LinkedList()
ll.push_to_list(1)
ll.push_to_list(2)
ll.push_to_list(3)
ll.push_to_list(4)
ll.push_to_list(5)
ll.push_to_list(6)
ll.push_to_list(7)
ll.push_to_list(8)
ll.printList()
ll.find_mid_ele()
ll.find_mid_by_count()
ll.find_mid_by_floyds_cycle()
ll.find_mid_by_counter()

    