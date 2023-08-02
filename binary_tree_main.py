from binary_search_tree import *

#inserting 10 node to tree using for loop and range method
node = None
for i in range(1, 11):
    node = insert(node, i)

print("---Traversing in pre order manner through tree node---")
pre_order_traversal(node)
print()

print("---Traversing in in-order manner through tree node---")
in_order_traversal(node)
print()

print("---Traversing in post-order manner through tree node---")
post_order_traversal(node)
print()

#Searching the number from the keyboard
num = int(input("Please any number to search in the tree:- "))
num_node = search_node_by_data(node, num)
print("---Displaying the node that contain the user number")
print("The node that contain that you entered is:- ", num_node)
print()

#searching minimum value and storing it min_value variable
min_value = find_min_value_node(node)
print("---Displaying minimum value in the tree---")
print("minimum value is:- ", min_value.data)

#searching maximum vale and storing it max_value variable
max_value = find_max_value_node(node)
print("---Displaying maximum value in the tree---")
print("Maximum value is:- ", max_value.data)
print()

#deleting node by its value 
value = int(input("Please enter value of the node that you want to delete:- "))
node = delete_node_by_data(node, value)   
print("--Displaying tree after deleting node---")
in_order_traversal(node)