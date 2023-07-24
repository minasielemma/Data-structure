from single_linked_list import Node

class CircularLinkedList:
    """Circular linked list operation"""
    def __init__(self):
        self.head:Node= None
    
    def count_nodes(self):
        """counting number of node at circular linked list"""
        if self.head is None:
            return 0
        count = 0
        current_node = self.head
        while True:
            count += 1
            current_node = current_node.next
            if current_node is self.head:
                break
        return count
    
    def display(self):
        """Displaying the content of data"""
        current_node = self.head
        while True:
            print(f"Node[Data: {current_node.data}]")
            current_node = current_node.next
            if current_node is self.head:
                break               
    
    def insert_at_end(self, data):
        """inserting node at the end of the list"""
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            current_node = self.head
            while current_node.next is not self.head:
                current_node = current_node.next
            new_node = Node(data)
            current_node.next = new_node
            new_node.next = self.head
    
    def inset_at_beginning_of_list(self, data):
        """inserting data at the beginning of the list"""
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            current_node = self.head
            while current_node.next is not self.head:
                current_node = current_node.next
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
            current_node.next = self.head
    
    def delete_at_beginning_of_list(self):
        """Deleting node from the beginning of the list"""
        if self.head is None:
            print("There is no node at the list")
            return 
        current_node = self.head
        while current_node.next is not self.head:
            current_node = current_node.next
        self.head = self.head.next
        current_node.next = self.head
    
    def delete_at_end_of_list(self):
        """Deleting node from the end of the list"""
        if self.head is None:
            print("There is no node at the list")
            return
        current_node = self.head
        previous_node = self.head
        while current_node.next is not self.head:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = self.head
        
            