###
### Unit 8
###


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


""" 
Problem 4: Find Leftmost Node I
Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

Evaluate the time complexity of your function.

Understand:
    - By "leftmost node", do we mean the node furthest to the left at any level?
    - How should we handle an empty tree (null root)?

Plan:
    - Implement an iterative approach using a queue
    - Traverse the tree level by level, always prioritizing the left child
    - Return the value of the leftmost node
    - Time complexity: O(h) where h is the height of the tree
"""
# Implement
from collections import deque

def left_most(root):
    # Handle empty tree
    if not root:
        return None
    
    # Iterative approach with queue
    queue = deque([root])
    leftmost = root.val
    
    while queue:
        node = queue.popleft()
        
        # Update leftmost if we're at a new level's leftmost node
        if node == queue[0] if queue else True:
            leftmost = node.val
            
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return leftmost

# Time complexity: O(n) where n is the number of nodes in the tree


""" 
Problem 5: Find Leftmost Node II
If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of the function.

Understand:
    - How do we track the leftmost node recursively?
    - Does the leftmost node mean the node furthest to the left at the lowest level?

Plan:
    - Implement a recursive approach with a helper function
    - Track the current depth and update leftmost node when we find a deeper left path
    - Return the leftmost node value
    - Time complexity: O(n) where n is the number of nodes
"""
# Implement
def left_most(root):
    if not root:
        return None
    
    result = [None, -1]  # [leftmost_value, max_depth]
    
    def dfs(node, depth):
        if not node:
            return
            
        # Update result if we've found a deeper leftmost node
        if depth > result[1]:
            result[0] = node.val
            result[1] = depth
            
        # Traverse left first, then right
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    
    dfs(root, 0)
    return result[0]

# Time complexity: O(n) where n is the number of nodes in the tree


""" 
Problem 6: Is Uni-valued
A binary tree is uni-valued if every node in the tree has the same value. Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.

Evaluate the time complexity of your solution.

Understand:
    - Do we consider an empty tree to be uni-valued?
    - What about a tree with only one node?

Plan:
    - Store the value of the root node
    - Traverse the tree and check if all nodes have the same value
    - Return False as soon as we find a different value
    - Return True if we complete the traversal without finding different values
    - Time complexity: O(n) where n is the number of nodes
"""
# Implement
def is_univalued(root):
    if not root:
        return True
    
    # Get the target value from root
    target_val = root.val
    
    def check_nodes(node):
        if not node:
            return True
        
        # Check if current node matches the target value
        if node.val != target_val:
            return False
            
        # Recursively check left and right subtrees
        return check_nodes(node.left) and check_nodes(node.right)
    
    return check_nodes(root)

# Time complexity: O(n) where n is the number of nodes in the tree


""" 
Problem 7: Binary Tree Height
Given the root of a binary tree, write a function height() that returns the height of a binary tree.

Evaluate the time complexity of your function.

Understand:
    - Is the height of an empty tree 0 or -1?
    - Is a tree with only a root considered height 1?

Plan:
    - Use a recursive approach to calculate height
    - For each node, calculate the height of left and right subtrees
    - Return the maximum of the two heights + 1
    - Base case: return 0 for null nodes
    - Time complexity: O(n) where n is the number of nodes
"""
# Implement
def height(root):
    if not root:
        return 0
    
    # Calculate height of left and right subtrees
    left_height = height(root.left)
    right_height = height(root.right)
    
    # Return the maximum height + 1 for the current node
    return max(left_height, right_height) + 1

# Time complexity: O(n) where n is the number of nodes in the tree


""" 
Problem 8: BST Insert
Given the root of a binary search tree, insert a new node with a given key and value into the tree. Return the root of the modified tree. The tree is sorted by key. If a node with the given key already exists, update the the existing key's value. You do not need to maintain a balanced tree.

Evaluate the time complexity of your function.

Understand:
    - Should we modify the tree in-place or create a new tree?
    - How should we handle duplicate keys?

Plan:
    - Traverse the BST to find the correct insertion point based on key
    - If a node with the key already exists, update its value
    - Otherwise, create a new node and insert it as a leaf
    - Return the root of the modified tree
    - Time complexity: O(h) where h is the height of the tree
"""
# Implement
def insert(root, key, value):
    # If tree is empty, create a new root node
    if not root:
        return TreeNode(key, value)
    
    # If key already exists, update the value
    if key == root.key:
        root.val = value
    # If key is smaller, insert in left subtree
    elif key < root.key:
        root.left = insert(root.left, key, value)
    # If key is larger, insert in right subtree
    else:
        root.right = insert(root.right, key, value)
    
    return root

# Time complexity: O(h) where h is the height of the tree (worst case O(n) for unbalanced tree)


""" 
Problem 9: BST Remove I
Use the provided pseudocode to solve the problem below. Given a key and the root of a binary search tree, remove the node with the given key. Return the root of the modified tree.

Understand:
    - How do we handle the case when the node to remove has two children?
    - What if the key doesn't exist in the tree?

Plan:
    - Follow the provided pseudocode:
    - Locate the node to be removed through BST search
    - Handle different cases: leaf node, node with one child, node with two children
    - For a node with two children, find the in-order successor and use it as replacement
    - Time complexity: O(h) where h is the height of the tree
"""
# Implement
def remove_bst(root, key):
    # Base case: if root is None, the key doesn't exist in the tree
    if not root:
        return None
    
    # Locate the node to be removed
    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:
        # Node to remove found
        
        # Case 1: Leaf node (no children)
        if not root.left and not root.right:
            return None
            
        # Case 2: Node with only one child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
            
        # Case 3: Node with two children
        # Find the in-order successor (smallest node in right subtree)
        successor = find_min(root.right)
        
        # Replace the node's key and value with the successor's
        root.key = successor.key
        root.val = successor.val
        
        # Remove the successor
        root.right = remove_bst(root.right, successor.key)
    
    return root

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

# Time complexity: O(h) where h is the height of the tree


""" 
Problem 10: BST In-order Successor
In the remove_bst() problem, we summarized the in-order successor of a given node as the smallest node in the given node's right subtree. This is true if the given node has a right subtree.

Understand:
    - What if the node doesn't have a right subtree?
    - How do we find the successor in that case?

Plan:
    - If the current node has a right subtree, find the minimum node in that subtree
    - Otherwise, the successor is the nearest ancestor where current is in its left subtree
    - Traverse from root keeping track of a potential successor
    - Time complexity: O(h) where h is the height of the tree
"""
# Implement
def inorder_successor(root, current):
    # Case 1: If current has a right subtree, successor is the minimum in that subtree
    if current.right:
        return find_min(current.right)
    
    # Case 2: If no right subtree, find the nearest ancestor where current is in its left subtree
    successor = None
    ancestor = root
    
    while ancestor != current:
        if current.key < ancestor.key:
            successor = ancestor
            ancestor = ancestor.left
        else:
            ancestor = ancestor.right
    
    return successor

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

# Time complexity: O(h) where h is the height of the tree