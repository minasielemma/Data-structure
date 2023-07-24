from double_linked_list import DoubleLinkedList

dl = DoubleLinkedList()

#adding data at beginning of the list
for i in range(1, 10):
    dl.insert_at_beginning(i)

print("----Displaying data after adding at beginning of the list ---")
dl.display()   

#adding node at the end of the list
for i in range(11, 19):
    dl.inset_at_end(i)

print("---Displaying data after adding at the end of the list---")
dl.display()

#adding the element using given index
dl.insert_node_at_meddle(12, 4)

print("---Displaying the list after adding element by given index---")
dl.display()

#deleting element at beginning of the linked list
dl.delete_first_node()

print("---Displaying the list after deleting element from the head---")
dl.display()

#deleting element at the end of the linked list
dl.delete_last_node()

print("---Displaying the list after deleting element for the end---")
dl.display()

#deleting element at given index
dl.delete_using_index(3)

print("---Displaying the list after deleting element using index---")
dl.display()

#deleting element using data
dl.delete_node_by_data(14)

print("---Displaying the list after deleting element using data---")
dl.display()