class BinaryTreeNode:
    """class for binary tree node"""
    def __init__(self, data):
        self.data = data
        self.left:BinaryTreeNode = None
        self.right:BinaryTreeNode = None
        
    def set_data(self, data):
        """Setting data for node"""
        self.data = data
    
    def get_data(self):
        """Return data"""
        return self.data
    
    def set_left_node(self, left_node):
        """Setting left node"""
        self.left = left_node
    
    def get_left_node(self):
        """Return left node"""
        return self.left
    
    def set_right_node(self, right_node):
        """Setting right node"""
        self.right = right_node
        
    def get_right_node(self):
        """Return right node"""
        return self.right
    
    def __str__(self):
        return f"Node[{self.data}]"
def insert(root:BinaryTreeNode, data):
    """Inserting node to tree"""
    if not root:
        return BinaryTreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root
    
def pre_order_traversal(root:BinaryTreeNode):
    """Traversing in pre-order"""
    if root:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def in_order_traversal(root:BinaryTreeNode):
    """Traversing in order manner"""
    if root:
        in_order_traversal(root.left)
        print(root.data) 
        in_order_traversal(root.right)   

def post_order_traversal(root:BinaryTreeNode):
    """Traversing in Post order manner"""
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)

def search_node_by_data(root:BinaryTreeNode, data):
    """search node through binary tree using data"""
    if root is None or root.data == data:
        return root
    if data < root.data:
        return search_node_by_data(root.get_left_node(), data)
    else:
        return search_node_by_data(root.get_right_node(), data)

def find_max_value_node(root:BinaryTreeNode):
    """searching for maximum value holder node in the tree"""
    if root is None:
        return None
    current = root
    while current.get_right_node() is not None:
        current = current.get_right_node()
    return current

def find_min_value_node(root:BinaryTreeNode):
    """search for node that holds minimum value"""
    if root is None:
        return None
    current = root
    while current.get_left_node() is not None:
        current = current.get_left_node()
    return current 

def delete_node_by_data(root: BinaryTreeNode, data) -> BinaryTreeNode:
    """Deleting node by its node data"""
    if root is None:
        return None
    parent = None
    current = root

    while current is not None and current.get_data() != data:
        parent = current
        if data < current.get_data():
            current = current.get_left_node()
        else:
            current = current.get_right_node()

    if current is None:
        print("--- Node doesn't exist ---")
        return root

    if current.get_left_node() is None and current.get_right_node() is None:
        if parent is None:
            return None
        elif parent.get_left_node() == current:
            parent.set_left_node(None)
        else:
            parent.set_right_node(None)
        return root

    if current.get_left_node() is None:
        child = current.get_right_node()
    elif current.get_right_node() is None:
        child = current.get_left_node()
    else:
        successor_parent = current
        successor = current.get_right_node()

        while successor.get_left_node() is not None:
            successor_parent = successor
            successor = successor.get_left_node()

        current.set_data(successor.get_data())

        if successor_parent.get_left_node() == successor:
            successor_parent.set_left_node(successor.get_right_node())
        else:
            successor_parent.set_right_node(successor.get_right_node())
        return root

    if parent is None:
        return child
    elif parent.get_left_node() == current:
        parent.set_left_node(child)
    else:
        parent.set_right_node(child)

    return root