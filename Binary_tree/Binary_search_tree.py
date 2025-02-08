class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        #if data is already equal or exist in the tree ingnore 
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)
                
    def in_order_recursive(self):
        elements = []

        if self.left:
            #add all elements of array to elements
            elements += self.left.in_order_recursive()
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_recursive()
        return elements
    def in_order_iterative(self):
        elements = []
        node_data = []
        current = self
        while current or node_data:
            if current:
                node_data.append(current)
                current = current.left
                
            else:
                current = node_data.pop()
                elements.append(current.data)
                current = current.right
        return elements
        
    # pre order recursive method
    def pre_order_recursive(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_recursive()
        if self.right:
            elements += self.right.pre_order_recursive()
        return elements
    def pre_order_iterative(self):
        elements = []
        node_data = []
        current = self
        
        while current or node_data:
            if current:
                elements.append(current.data)
                node_data.append(current)
                current = current.left
                
            else:
                current = node_data.pop()
                current = current.right
        return elements
    #post order recursive method
    def post_order_recursive(self):
        elements = []
        if self.left:
            elements += self.left.pre_order_recursive()
        if self.right:
            elements += self.right.pre_order_recursive()
        elements.append(self.data)
        return elements
    def post_order_iterative(self):
        elements = []
        node_data = []
        current = self
        while current or node_data:
            if current:
                node_data.append(current)
                current = current.left
            else:
                current = node_data.pop()
                current = current.right
            elements.append(current.data)
        return elements

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        return False
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
def build_binary(arr):
    root = BinaryTree(arr[0])
    for i in range(1,len(arr)):
        root.add_child(arr[i])
    return root
    
    
if __name__ == '__main__':
    numbers= [15,12,7,14,27,20,23,88 ]
    tree = build_binary(numbers)
    print("in order recursive method",tree.in_order_recursive())
    print("in order iterative method",tree.in_order_iterative())
    print("pre order recursive method",tree.pre_order_recursive())
    print("pre order iterative method",tree.pre_order_iterative())
    print("post order recursive method",tree.post_order_recursive())
    print("post order iterative method",tree.post_order_iterative())
    print(tree.search(400))
    print(tree.find_min())
    print(tree.find_max())


