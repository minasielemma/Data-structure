
#node for single linked list
class Node:
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None
    def set_data(self, data):
        """Setting data """
        self.data = data
    
    def get_data(self):
        """getting data"""
        return self.data
    
class LinkedList:
    """Linked List class"""
    def __init__(self):
        self.head = None
        
    def append(self, data):
        """insert into linked list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def display(self):
        """displaying all list"""
        current = self.head
        print(f"Length of the list: {self.list_length()}")
        if current is None:
            print("The list is empty")
        while current is not None:
            print(f"Node[data : {current.data}]")
            current = current.next
        
    def list_length(self):
        """length of linked list"""
        current = self.head
        count = 0    
        if current is None:
            return 0
        while current is not None:
            count = count + 1
            current = current.next
        return count
    
    def insert_at_beginning(self,data):
        """inserting data at beginning of the linked list"""
        new_node = Node(data)
        if self.list_length() == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_middle(self, pos, data):
        """insert at middle of linked list"""
        if pos == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data);
            count = 0
            current = self.head
            while count < pos-1:
                count += 1
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def delete_first_node(self):
        """deleting first node"""
        if self.list_length() == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            
    def delete_last_node(self):
        """deleting last node"""
        if self.list_length() == 0:
            print("The list is empty")
        else:
            current = self.head
            previous_node = self.head
            while current.next is not None:
                previous_node = current
                current = current.next   
            previous_node.next = None
            
    def delete_middle_node(self, pos):
        """deleting node at middle node"""
        if self.list_length() == 0:
            print("The list is empty")
        elif pos > self.list_length() or pos < 0:
            print("The position does not exist. Please enter a valid position")
        elif pos == 0:
            self.delete_first_node()
        else:
            current_node = self.head
            count = 0
            while count < pos - 1:
                count += 1
                current_node = current_node.next
            temp = current_node.next
            current_node.next = temp.next
    
    def delete_node_by_value(self, value):
        """deleting node by value"""
        if self.list_length() == 0:
            print("The list is empty")
        else:
            current_node = self.head
            previous_node = self.head
            while current_node.next is not None:
                if current_node.data == value:
                    previous_node.next = current_node.next
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next
    
    def clear(self):
        """deleting all data"""
        self.head = None
                
            
        