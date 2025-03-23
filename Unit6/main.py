###
### Unit 6
###


""" 
Problem X:


Understand:
    - Share 2 questions you would ask to help understand the question

Plan:
    - Write out in plain English what you want to do
    - Translate each sub-problem into pseudocode

Implement:
    - Translate the pseudocode into Python and share your final answer
"""


""" 
Problem 1: Nested Constructors

Understand:
    - We need to create a linked list with the values 4 -> 3 -> 2 using a single assignment statement
    - We'll use the nested constructors approach, creating nodes inside other nodes

Plan:
    - Use the Node constructor to create the 2 node
    - Nest that inside the constructor for the 3 node
    - Nest that inside the constructor for the 4 node
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Create linked list 4 -> 3 -> 2 in a single statement
head = Node(4, Node(3, Node(2)))


""" 
Problem 2: Find Frequency

Understand:
    - We need to count occurrences of a specific value in a linked list
    - Input: head node of a linked list and a value to search for
    - Output: count of how many times the value appears in the list

Plan:
    - Traverse the linked list from head to tail
    - Keep a counter for occurrences of the target value
    - Return the final count
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_element(head, val):
    count = 0
    current = head
    
    # Traverse the list
    while current:
        if current.value == val:
            count += 1
        current = current.next
    
    return count

# Time Complexity: O(n) where n is the length of the linked list. We need to visit each node once.
# Space Complexity: O(1) as we only use a constant amount of extra space regardless of input size.


""" 
Problem 3: Remove Tail

Understand:
    - We need to fix a bug in the remove_tail function
    - The function should remove the last node of a linked list
    - Current bug: The function finds the last node instead of the second-to-last node

Plan:
    - Fix the while loop condition to stop at the second-to-last node
"""
# Implement
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
    
    # Start from the head and find the second-to-last node
    current = head
    while current.next.next: # Fixed: Stop at second-to-last node
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node's next to None
    return head


""" 
Problem 4: Find the Middle

Understand:
    - We need to find the middle node of a linked list using the slow-fast pointer technique
    - If there are two middle nodes, return the second middle node
    - Need to analyze time and space complexity

Plan:
    - Use two pointers: slow moves one step at a time, fast moves two steps
    - When fast reaches the end, slow will be at the middle
"""
# Implement
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Time Complexity: O(n) where n is the length of the linked list. The fast pointer traverses the list at twice the speed.
# Space Complexity: O(1) as we only use a constant amount of extra space.


