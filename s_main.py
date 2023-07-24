from single_linked_list import *

sl = LinkedList()
#adding data at beginning of the list
for i in range(1, 10):
    sl.insert_at_beginning(i)
    
print("----Displaying data after adding at beginning of the list ---")
sl.display() 

#adding node at the end of the list 
for i in range(11, 20):
    sl.append(i)
    
print("---Displaying data after adding at the end of the list---")
sl.display()
    
#adding the element using given index
sl.insert_at_middle(4, 30)

print("---Displaying the list after adding element by given index---")

sl.display()

#deleting element at beginning of the linked list
sl.delete_first_node()

print("---Displaying the list after deleting element from the head---")
sl.display()

#deleting element at the end of the linked list
sl.delete_last_node()

print("---Displaying the list after deleting element for the end---")

sl.display()

#deleting element at given index
sl.delete_middle_node(6)

print("---Displaying the list after deleting element using index---")

sl.display()

#deleting list node using data
sl.delete_node_by_value(14)


print("---Displaying the list after deleting node by value")
sl.display()
    