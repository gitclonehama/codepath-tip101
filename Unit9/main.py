###
### Unit 9
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
Problem 1: Is Symmetric Tree
Given the root of a binary tree, return True if the tree's left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). Return False otherwise.

Understand:
    - How do we define "mirror" of subtrees? Does it mean same structure with identical values?
    - How should we handle null/None nodes? Are they considered symmetric with other null nodes?

Plan:
    - Create a helper function to check if two subtrees are mirrors of each other
    - Two trees are mirrors if:
        - Their root values are the same
        - Left subtree of first tree mirrors right subtree of second tree
        - Right subtree of first tree mirrors left subtree of second tree
    - Use recursion to check each level of the tree
"""
# Implement
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    
    def are_mirrors(left, right):
        # If both are None, they're symmetric
        if not left and not right:
            return True
            
        # If only one is None, they're not symmetric
        if not left or not right:
            return False
            
        # Check current values and recursive structure
        return (left.val == right.val and 
                are_mirrors(left.left, right.right) and 
                are_mirrors(left.right, right.left))
    
    # Check if left and right subtrees are mirrors
    return are_mirrors(root.left, root.right)

# Time Complexity: O(n) where n is the number of nodes in the tree


""" 
Problem 2: Root-to-Leaf Paths
Given the root of a binary tree, return a list of all root-to-leaf paths in any order.
A leaf is a node with no children.

Understand:
    - What format should the paths be in? String format with "->" as separator?
    - Should we handle empty trees specially? What should be returned?

Plan:
    - Use a depth-first search (DFS) approach with backtracking
    - Maintain a current path as we traverse the tree
    - When we reach a leaf node (no children), add the current path to our result
    - Use recursion to explore all possible paths from root to leaves
"""
# Implement
def binary_tree_paths(root):
    if not root:
        return []
    
    paths = []
    
    def dfs(node, path):
        # Add current node to path
        if path:
            path += "->" + str(node.val)
        else:
            path = str(node.val)
        
        # If leaf node (no children), add path to results
        if not node.left and not node.right:
            paths.append(path)
            return
        
        # Recursively explore children
        if node.left:
            dfs(node.left, path)
        if node.right:
            dfs(node.right, path)
    
    dfs(root, "")
    return paths

# Time Complexity: O(n) to visit all nodes, with extra string operations making it O(n²) in total


""" 
Problem 3: Minimum Difference in BST
Given the root of a binary search tree, return the minimum difference between the values of any two different nodes in the tree.

Understand:
    - Can we leverage BST properties (all left nodes < parent < all right nodes)?
    - Will there always be at least two nodes in the tree?

Plan:
    - Use in-order traversal of the BST to get values in sorted order
    - Keep track of the previous node's value during traversal
    - Calculate difference between current and previous nodes
    - Update minimum difference if current difference is smaller
"""
# Implement
def min_diff_in_bst(root):
    prev_val = float('-inf')  # Initialize with negative infinity
    min_diff = float('inf')   # Initialize with positive infinity
    
    def inorder(node):
        nonlocal prev_val, min_diff
        if not node:
            return
        
        # Process left subtree
        inorder(node.left)
        
        # Process current node
        if prev_val != float('-inf'):
            min_diff = min(min_diff, node.val - prev_val)
        prev_val = node.val
        
        # Process right subtree
        inorder(node.right)
    
    inorder(root)
    return min_diff

# Time Complexity: O(n) where n is the number of nodes in the BST


""" 
Problem 4: Increasing Order Search Tree
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node of the tree is now the root of tree and every node has no left child and only one right child.

Understand:
    - Do we need to create new nodes or reuse existing ones?
    - Should we modify the tree in-place or create a new structure?

Plan:
    - Perform an in-order traversal to visit nodes in ascending order
    - Create a dummy node to start the new tree
    - As we visit each node, set it as the right child of our current position
    - Reset each node's left child to None
    - Advance our current position pointer
"""
# Implement
def increasing_bst(root):
    dummy = TreeNode()  # Dummy node to start with
    current = dummy
    
    def inorder(node):
        nonlocal current
        if not node:
            return
        
        # Process left subtree first
        inorder(node.left)
        
        # Process current node
        node.left = None          # Remove left child
        current.right = node      # Attach to right of our current position
        current = node            # Update current position
        
        # Process right subtree
        inorder(node.right)
    
    inorder(root)
    return dummy.right  # Return the actual root (skip dummy)

# Time Complexity: O(n) where n is the number of nodes in the BST


""" 
Problem 5: Equal Tree Split
Given the root of a binary tree, return True if removing an edge between two nodes can split the tree into two trees with an equal number of nodes. Return False otherwise.

Understand:
    - Can any edge be removed, or just edges from the root?
    - What happens if the tree has an odd number of nodes?

Plan:
    - Count total nodes in the tree first
    - If total is odd, return False (can't split evenly)
    - Traverse the tree again, calculating size of each subtree
    - If any subtree has exactly half the total nodes, return True
"""
# Implement
def can_split(root):
    # Count total nodes
    def count_nodes(node):
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    total_nodes = count_nodes(root)
    
    # If odd number of nodes, can't split evenly
    if total_nodes % 2 != 0:
        return False
    
    target = total_nodes // 2
    found = False
    
    # Check if any subtree has exactly half the nodes
    def size_and_check(node):
        nonlocal found
        if not node or found:
            return 0
        
        left_size = size_and_check(node.left)
        right_size = size_and_check(node.right)
        
        subtree_size = 1 + left_size + right_size
        
        # Check if removing edge above this node would create equal split
        if subtree_size == target:
            found = True
        
        return subtree_size
    
    size_and_check(root)
    return found

# Time Complexity: O(n) where n is the number of nodes in the tree


""" 
Problem 6: Level Order Traversal of Binary Tree
Given the following pseudocode and the root of a binary tree, return a list of the level order traversal of it's nodes' values (i.e., from left to right, level by level).

Understand:
    - We need to traverse the tree one level at a time, from top to bottom
    - At each level, we process nodes from left to right before moving to the next level

Plan:
    - Use a queue data structure to track nodes at each level
    - Process the tree using Breadth-First Search (BFS) approach
    - Store visited node values in a result list
"""
# Implement
from collections import deque

def level_order(root):
    # If the tree is empty:
    if not root:
        return []  # return an empty list

    # Create an empty queue using deque
    queue = deque([root])
    # Create an empty list to store the explored nodes
    result = []

    # While the queue is not empty:
    while queue:
        # Pop the next node off the queue (pop from the left side!)
        node = queue.popleft()
        # Add the popped node to the list of explored nodes
        result.append(node.val)

        # Add each of the popped node's children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # Return the list of visited nodes
    return result

# Time Complexity: O(n) where n is the number of nodes in the tree
# We visit each node exactly once, and the operations for each node (enqueue, dequeue, append to result)
# are all constant time O(1) operations.


""" 
Problem 7: Find Minimum Depth of Binary Tree
Given the root of a binary tree, return its minimum depth. The minimum depth is the number of nodes along the shortest path from the root down to the nearest leaf node.

Understand:
    - The minimum depth is the shortest path from root to any leaf node
    - A leaf node is a node with no children (no left and no right child)
    - We need to find the leaf node with the smallest depth

Plan:
    - Use BFS to traverse the tree level by level
    - As soon as we encounter a leaf node, return its depth
    - BFS ensures we find the first leaf node at the minimum depth
"""
# Implement
def min_depth(root):
    if not root:
        return 0
    
    # Use BFS to find the first leaf node
    queue = deque([(root, 1)])  # Store (node, depth) pairs
    
    while queue:
        node, depth = queue.popleft()
        
        # Check if this is a leaf node
        if not node.left and not node.right:
            return depth
        
        # Add children to queue with incremented depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0  # Should not reach here if tree is valid

# Time Complexity: O(n) in worst case, where n is the number of nodes in the tree
# In the worst case scenario, the first leaf might be at the maximum depth, requiring us to visit 
# most nodes. However, we often terminate early once we find the first leaf.


