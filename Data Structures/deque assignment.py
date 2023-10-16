#Explain the concept of queues in Python. How is it different from other data structures like lists and arrays?
#Give an example of a queue and demonstrate how to access and modify its elements.

from collections import deque

# Create an empty queue to represent a bank customer queue
bank_queue = deque()

# Customers arrive and join the queue
bank_queue.append("Customer 1")
bank_queue.append("Customer 2")
bank_queue.append("Customer 3")
bank_queue.append("Customer 4")
bank_queue.append("Customer 5")

# Calculate the size (number of customers) in the queue
queue_size = len(bank_queue)

print("Number of Customers in the Bank Queue:", queue_size)

# A bank teller serves the next customer (FIFO)
served_customer = bank_queue.popleft()
print("Served Customer:", served_customer)