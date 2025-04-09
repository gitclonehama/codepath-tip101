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


""" 
Problem 2: 3-Node Sum I
Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Understand:
    - Can we assume the tree will always have exactly 3 nodes (root + 2 children)?
    - Do we need to handle any edge cases like None values?

Plan:
    - Check if the root value equals the sum of root.left.val and root.right.val
    - Return True if they're equal, False otherwise
    - Time complexity: O(1) as we're only doing a simple comparison
"""
# Implement
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    # Simple check if root value equals sum of children's values
    return root.val == root.left.val + root.right.val

# Time complexity: O(1) - constant time operation regardless of input size


""" 
Problem 3: 3-Node Sum II
Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.

Understand:
    - What if the tree has fewer than 3 nodes (only root, or root with one child)?
    - Should we return False if one or both children are missing?

Plan:
    - Check if the root is None, return False if it is
    - Calculate sum of children values, handling None cases
    - Compare root value with sum and return result
    - Time complexity: O(1) as we're only doing simple checks and comparisons
"""
# Implement
def check_tree(root):
    # Handle edge cases
    if root is None:
        return False
    
    # Calculate sum of children's values, handling None cases
    left_val = root.left.val if root.left else 0
    right_val = root.right.val if root.right else 0
    
    # Check if root has at least one child before comparing
    if root.left is None and root.right is None:
        return False
        
    return root.val == left_val + right_val

# Time complexity: O(1) - constant time operations


