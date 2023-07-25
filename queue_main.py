from queue import Queue

#initializing queue
queue = Queue(10)

#inserting element to queue from 1 upto 9 using range function and for loop. 
for i in range(1, 10):
    queue.enqueue(i)
print("---Displaying element after queueing 10 element")
queue.display()
print()

#queueing one element to queue
queue.enqueue(10)
print("---Displaying after inserting one element to queue")
queue.display()
print()

#displaying front element of queue
print(f"Front element is: {queue.get_front()}")
print()

#displaying rear element of queue
print(f"Rear element is: {queue.get_rear()}")
print()

#displaying size of queue
print(f"Size of element is: {queue.get_size()}")
print()

#deleting one element from queue
queue.dequeue()
print("---Displaying queue after deleting or removing one element")
queue.display()
print(f"Size of element is: {queue.get_size()}")
print()

#deleting all element using loop 
while queue.get_size() != 0:
    print(f"{queue.dequeue()} deleted")
print()
print("---Displaying queue after deleting or removing all element")
queue.display()
print(f"Size of element is: {queue.get_size()}")
print()
