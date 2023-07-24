from circular_linked_list import CircularLinkedList

#for delete and insert operation at the middle of the list please refer single list operation. Almost they are the same
cl = CircularLinkedList()
#inserting node at the beginning of the list
for i in range(1,11):
    cl.inset_at_beginning_of_list(i)

print("---Displaying content of the list after inserting node at the beginning of the list")
print(f"Number of the node: {cl.count_nodes()}")
cl.display()

#inserting node at the end of the list
for i in range(11,21):
    cl.insert_at_end(i)
    
print("---Displaying content of the list after inserting node at the end of the list")
print(f"Number of the node: {cl.count_nodes()}")
cl.display()

#deleting node form the beginning of the list
cl.delete_at_beginning_of_list()
print("---Displaying content of the list after deleting node at the beginning of the list")
print(f"Number of the node: {cl.count_nodes()}")
cl.display()

#deleting node at the end of the list
cl.delete_at_end_of_list()
print("---Displaying content of the list after deleting node at the end of the list")
print(f"Number of the node: {cl.count_nodes()}")
cl.display()
