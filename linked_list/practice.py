class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtEnd(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            tmp = self.head
            print(tmp.data,"tmp")
            while tmp.next is not None:
                tmp = tmp.next
                print(tmp.data)
            tmp.next = node
    def printLinkedList(self):
        node = self.head
        while node is not None:
            print(f"-->{node.data}",end="")
            node = node.next
ll = LinkedList()
print(ll.head,"head")
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(3)
ll.insertAtEnd(3)

# ll.printLinkedList()
