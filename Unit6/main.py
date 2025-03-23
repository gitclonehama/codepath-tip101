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


