
class DoubleLinkNode:
    """class for double linked list node"""
    def __init__(self, data=None, next_node=None, prev_node = None):
        self.data = data
        self.next_node:DoubleLinkNode = next_node
        self.prev_node:DoubleLinkNode = prev_node
    
    def set_data(self, data):
        """set data for node"""
        self.data = data
        
    def get_data(self):
        """getting data"""
        return self.data
    
    def set_next_node(self, next_node):
        """setting next node"""
        self.next_node = next_node
        
    def get_next_node(self):
        """getting next node"""
        return self.next_node
    
    def has_next_node(self):
        """checking whether node has next node or not"""
        return self.next_node is not None

    def set_prev_node(self, prev_node):
        """setting prev node"""
        self.prev_node = prev_node
        
    def get_prev_node(self):
        """getting prev node"""
        return self.prev_node
    
    def has_prev_node(self):
        """checking whether node has prev node or not"""
        return  self.prev_node is not None
    
    def __str__(self):
        return "Node[Data = %s]" % {self.data}
    
class DoubleLinkedList:
    """double linked list operation"""
    def __init__(self,head=None, tail=None):
        self.head:DoubleLinkNode = head
        self.tail:DoubleLinkNode = tail
        
    def display(self):
        """Displaying all list content"""
        print(f"head: {self.head}")  
        print(f"tail: {self.tail}")
        current = self.head
        while current is not None:
            print(current)
            current = current.get_next_node()
            
    def length(self):
        """getting length of the list"""
        count = 0
        current = self.head
        if current is None:
            return 0
        while current.get_next_node() is not None:
            count += 1
            current = current.get_next_node()
        return count
            
    def insert_at_beginning(self, data):
        """inserting node at beginning of the list"""
        new_node = DoubleLinkNode(data=data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.set_prev_node(None)
            new_node.set_next_node(self.head)
            self.head.set_prev_node(new_node)
            self.head = new_node
    
    def inset_at_end(self, data):
        """inserting node at the end of the list"""
        if self.head is None:
            self.head=self.tail = DoubleLinkNode(data=data)
        else:
            current = self.head
            while current.get_next_node() is not None:
                current = current.get_next_node()
            current.set_next_node(DoubleLinkNode(data=data, next_node=None, prev_node=current))
            self.tail = current.get_next_node()
            
    def get_node(self, index):
        """getting node using index"""
        current_node = self.head
        if current_node is None:
            return None
        i = 0
        while i < index and current_node.get_next_node() is not None:
            current_node = current_node.get_next_node()
            if current_node is None:
                break
            i += 1
        return current_node
    def insert_node_at_meddle(self, data, pos:int):
        """inserting node at the meddle of the node"""
        if self.head is None:
            self.insert_at_beginning(data)
        elif pos > self.length() and pos < 0:
            print("Invalid index of the list")
        else:
            if self.head is None or pos == 0:
                self.insert_at_beginning(data)
            elif pos > 0:
                temp = self.get_node(pos)
                if temp is None or temp.get_next_node() is None:
                    self.inset_at_end(data)
                else:
                    new_node = DoubleLinkNode(data=data)
                    new_node.set_next_node(temp.get_next_node())
                    new_node.set_prev_node(temp)
                    temp.get_next_node().set_prev_node(new_node)
                    temp.set_next_node(new_node)
    
    def delete_first_node(self):
        """deleting node from head"""
        if self.head is None:
            print("There is no node at head of the list")
        else:
            self.head = self.head.get_next_node()
            self.head.set_prev_node(None)
            
    def delete_last_node(self):
        """deleting node from tail"""
        if self.head is None:
            print("There is no node at tail of the list")
        else:
            self.tail = self.tail.get_prev_node()
            self.tail.set_next_node(None)
    
    def delete_using_index(self, index):
        """deleting node using index"""
        if self.head is None:
            print("There is no node to delete")
        else:
            temp = self.get_node(index)
            temp.get_prev_node().set_next_node(temp.get_next_node())
            temp.get_next_node().set_prev_node(temp.get_prev_node())
            
    def delete_node_by_data(self, data):
        """deleting node by data"""
        if self.head is None:
            print("There is no Node to delete")
        else:
            current = self.head
            i = 0
            while(current.get_next_node() is not None):
                if current.data is data:
                    self.delete_using_index(i)
                    break
                i += 1
                current = current.get_next_node()
            else:
                print(f"There is node node that contain {data}")  
            

                
            
    