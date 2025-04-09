###
### Unit 8
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
Problem 1: Build a Binary Tree I
Given the following TreeNode class, create the binary tree depicted in the image below.

Binary Tree Example

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Understand:
    - What is the structure of the tree we need to build (since the image is not visible)?
    - Should we create a specific tree or demonstrate how to build a general binary tree?

Plan:
    - Create a binary tree with a root node and some children
    - Use the TreeNode class to instantiate nodes and connect them
    - Demonstrate how to build a simple binary tree with multiple levels
"""
# Implement
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a sample binary tree:
#      1
#     / \
#    2   3
#   / \   \
#  4   5   6

# Create leaf nodes first
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

# Create internal nodes
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, None, node6)

# Create root node
root = TreeNode(1, node2, node3)

# Function to verify the tree structure (for testing)
def print_tree(root):
    if root is None:
        return
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)

# Print the tree to verify
# print_tree(root)  # Output: 1 2 4 5 3 6


