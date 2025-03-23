###
### Unit 6
###


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


""" 
Problem 5: Is Palindrome?

Understand:
    - We need to check if a linked list represents a palindrome
    - A palindrome reads the same forward and backward
    - Need to analyze time and space complexity

Plan:
    - Find the middle of the linked list
    - Reverse the second half of the linked list
    - Compare the first half with the reversed second half
"""
# Implement
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True
    
    # Find the middle of the linked list
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    second_half = reverse_list(slow.next)
    
    # Compare the first and second half
    first_half = head
    while second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

# Time Complexity: O(n) where n is the length of the linked list
# Space Complexity: O(1) as we only modify the existing structure without using extra space


""" 
Problem 6: Detect Circular Linked List

Understand:
    - We need to determine if a linked list is circular
    - A circular linked list is one where the tail node points back to the head
    - Need to analyze time and space complexity

Plan:
    - Use the Floyd's Cycle Finding Algorithm (slow and fast pointers)
    - If pointers meet, check if the meeting point eventually leads back to head
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    if not head or not head.next:
        return False
    
    # Use Floyd's cycle finding algorithm
    slow = head
    fast = head
    
    # Detect if there's a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # If no cycle found
    if not fast or not fast.next:
        return False
    
    # Check if the cycle is circular (connects back to head)
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # If slow is head, then it's a circular list
    return slow == head

# Time Complexity: O(n) where n is the length of the linked list
# Space Complexity: O(1) as we only use two pointers


""" 
Problem 7: Find Last Node in a Linked List Cycle

Understand:
    - We need to find the last node in a cycle of a linked list
    - The last node is the one that points to a node in the cycle
    - If there's no cycle, return None

Plan:
    - First, detect if there's a cycle using Floyd's algorithm
    - If a cycle exists, find the start of the cycle
    - Find the last node in the cycle (the one that points to the start of the cycle)
"""
# Implement
def find_last_node_in_cycle(head):
    if not head or not head.next:
        return None
    
    # Detect cycle
    slow = head
    fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    
    if not has_cycle:
        return None
    
    # Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # The start of the cycle is now at slow/fast
    cycle_start = slow
    
    # Find the last node in the cycle (the one that points to cycle_start)
    current = cycle_start
    while current.next != cycle_start:
        current = current.next
    
    return current

# Time Complexity: O(n) where n is the length of the linked list
# Space Complexity: O(1) as we only use a constant amount of extra space


""" 
Problem 8: Partition List Around Value

Understand:
    - We need to partition a linked list around a value
    - All nodes with values less than the given value should come before nodes with values >= the given value
    - Need to maintain the original relative order within each partition

Plan:
    - Create two separate lists: one for values < val and one for values >= val
    - Connect the two lists at the end
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(head, val):
    if not head or not head.next:
        return head
    
    # Create dummy heads for our two partitions
    before_dummy = Node(0)
    after_dummy = Node(0)
    
    # Pointers to track the end of each partition
    before = before_dummy
    after = after_dummy
    
    # Traverse the original list
    current = head
    while current:
        if current.value < val:
            before.next = current
            before = before.next
        else:
            after.next = current
            after = after.next
        current = current.next
    
    # Connect the two partitions
    after.next = None
    before.next = after_dummy.next
    
    return before_dummy.next

# Time Complexity: O(n) where n is the length of the linked list
# Space Complexity: O(1) as we reuse the existing nodes


""" 
Problem 9: Convert Binary Number in a Linked List to Integer

Understand:
    - We need to convert a binary number represented as a linked list to an integer
    - Each node contains either 0 or 1
    - The most significant bit is at the head of the list

Plan:
    - Traverse the linked list
    - For each node, shift the result left by 1 and add the current node's value
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
    result = 0
    current = head
    
    while current:
        # Shift left and add current bit
        result = (result << 1) | current.value
        current = current.next
    
    return result

# Time Complexity: O(n) where n is the length of the linked list
# Space Complexity: O(1) as we only use a constant amount of extra space


""" 
Problem 10: Add Two Numbers Represented by Linked Lists

Understand:
    - We have two linked lists representing non-negative integers in reverse order
    - Each node contains a single digit
    - We need to add these numbers and return the sum as a linked list

Plan:
    - Traverse both lists simultaneously
    - Add the values along with any carry
    - Create new nodes for the result list
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_two_numbers(head_a, head_b):
    dummy = Node(0)
    current = dummy
    carry = 0
    
    p = head_a
    q = head_b
    
    while p or q:
        # Get the values or 0 if a list ends
        x = p.value if p else 0
        y = q.value if q else 0
        
        # Calculate sum and carry
        sum_val = x + y + carry
        carry = sum_val // 10
        
        # Create a new node for the result
        current.next = Node(sum_val % 10)
        current = current.next
        
        # Move to next nodes if they exist
        if p:
            p = p.next
        if q:
            q = q.next
    
    # If there's still a carry, add a new node
    if carry > 0:
        current.next = Node(carry)
    
    return dummy.next

# Time Complexity: O(max(m,n)) where m and n are the lengths of the two linked lists
# Space Complexity: O(max(m,n)) for the new list we're creating