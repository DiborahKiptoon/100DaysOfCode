import heapq

#Empty list epresenting the Max Binary Heap
max_heap = []

# Inserting elements with priority
heapq.heappush(max_heap, -30)  # Inserting with negative values for max priority
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -25)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -15)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -10)

# Retrieving the maximum element (with highest priority)
max_priority = -heapq.heappop(max_heap)
print("Max Element:", max_priority)  # Output: 30

# Change the priority of an element (e.g., from 25 to 35)
max_heap.remove(-25)  # Remove element with priority -25
heapq.heappush(max_heap, -35)  # Insert element with new priority -35

# Retrieve the maximum element after changing priority
max_priority = -max_heap[0]
print("Max Element after changing priority:", max_priority)  # Output: 35

# Remove an element (e.g., element with priority -10)
max_heap.remove(-10)  # Remove element with priority -10
max_priority = -heapq.heappop(max_heap)  # Extract the new maximum element
print("Removed Element:", max_priority)  # Output: 30 (element with priority -30)

# Retrieve the maximum element after removal
max_priority = -max_heap[0]
print("Max Element after removal:", max_priority)  # Output: 35

