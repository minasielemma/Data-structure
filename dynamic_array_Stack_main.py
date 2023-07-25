from dynamic_array_stack import Stack

#inserting 10 element using for loop
stack = Stack()
for i in range(1, 11):
    stack.push(i)
print("---Displaying element after inserting 1 upto 10 number")
stack.display()
print()

#insert one element to stack
stack.push(11)
print("---Displaying element after extending by one element to stack")
stack.display()
print()

#adding additional element to dynamic array stack
for i in range(11, 21):
    stack.push(i)
print("---Displaying element after inserting 11 upto 20 number")
stack.display()
print()

#print top element 
print("---Printing top element of the tack---")
print(stack.top())
print()

#removing each element one by one using for loop
print("---Displaying and removing each element from stack")
i = 1
for item in range(1, (len(stack.stack) +1)):
    print(i, "th element: ", stack.pop())
    i += 1
print()
    
print("---counting element after removing---")
print(stack.size())