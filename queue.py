class Queue:
    """class for Queue data structure using limited size"""
    def __init__(self, limit=5):
        self.queue = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
        
    def enqueue(self, data):
        """inserting data to queue"""
        if self.size >= self.limit:
            print("Queue overflow")
            return
        self.queue.append(data)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear += 1
        self.size += 1
        
    def dequeue(self):
        """Removing element from queue"""
        if self.size <= 0:
            print("Queue underflow")
            return
        data = self.queue.pop(0)
        self.size -= 1
        if self.size == 0:
            self.rear = self.front = None
        else:
            self.rear -= 1
        return data
    
    def get_rear(self):
        """Getting rear element from queue"""
        if self.rear is None:
            print("Queue is empty")
            return
        return self.queue[self.rear]
    
    def get_front(self):
        """Getting front element from queue"""
        if self.front is None:
            print("Queue is empty")
            return
        return self.queue[self.front]
    
    def get_size(self):
        """Getting size of queue"""
        return self.size
    
    def display(self):
        """Displaying element of queue using for loop"""
        for element in self.queue:
            print(f"Item[{element}]")
            