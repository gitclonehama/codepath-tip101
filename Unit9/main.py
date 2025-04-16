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


