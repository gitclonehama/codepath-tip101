###
### Unit 7
###


""" 
Problem 1: Hello Hello

Understand:
    - How does recursion work for repeating tasks?
    - How can we convert a recursive function into an iterative one?

Plan:
    - Implement the recursive function that prints "Hello" n times
    - Create an iterative version using a loop
    - Compare the two implementations
"""
# Implement
def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n - 1)

def repeat_hello_iterative(n):
    for i in range(n):
        print("Hello")

# Test both implementations
print("Recursive version:")
repeat_hello(5)
print("\nIterative version:")
repeat_hello_iterative(5)


""" 
Problem 2: Factorial Cases

Understand:
    - What is the base case for factorial?
    - How can we express factorial recursively?

Plan:
    - Define the base case: factorial(0) = 1
    - For n > 0, factorial(n) = n * factorial(n-1)
    - Implement the recursive function
"""
# Implement
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return n * factorial(n - 1)

# Test the function
print(f"Factorial of 5 is: {factorial(5)}")  # Expected: 120


""" 
Problem 3: Recursive Sum

Understand:
    - How can we calculate the sum of a list recursively?
    - What is the base case for an empty list?

Plan:
    - Define the base case: sum of empty list is 0
    - For non-empty list, sum = first element + sum of rest of list
    - Analyze time and space complexity
"""
# Implement
def sum_list(lst):
    # Base case: empty list
    if not lst:
        return 0
    # Recursive case: first element + sum of rest
    return lst[0] + sum_list(lst[1:])

# Test the function
test_list = [1, 2, 3, 4, 5]
print(f"Sum of {test_list} is: {sum_list(test_list)}")  # Expected: 15


""" 
Problem 4: Recursive Power of 2

Understand:
    - What are the properties of powers of 2?
    - How can we check if n is a power of 2 recursively?

Plan:
    - Define base cases:
      - If n = 1, return True (2^0 = 1)
      - If n < 1 or n has remainder when divided by 2, return False
    - Recursive case: Check if n/2 is a power of 2
"""
# Implement
def is_power_of_two(n):
    # Base cases
    if n <= 0:
        return False
    if n == 1:
        return True
    # If n is odd, it's not a power of 2
    if n % 2 != 0:
        return False
    # Recursive case: check if n/2 is a power of 2
    return is_power_of_two(n // 2)

# Test the function
print(f"Is 16 a power of 2? {is_power_of_two(16)}")  # Expected: True
print(f"Is 24 a power of 2? {is_power_of_two(24)}")  # Expected: False


""" 
Problem 5: Binary Search I

Understand:
    - How does binary search work on a sorted list?
    - What are the steps for an iterative implementation?

Plan:
    - Initialize left and right pointers
    - While left <= right:
      - Calculate middle index
      - If target found, return index
      - Adjust pointers based on comparison
    - Return -1 if target not found
"""
# Implement
def binary_search(lst, target):
    # Initialize pointers
    left = 0
    right = len(lst) - 1
    
    # While search space is not exhausted
    while left <= right:
        # Calculate middle index
        middle = (left + right) // 2
        
        # Check if target is at middle
        if lst[middle] == target:
            return middle
        # If target is greater, search right half
        elif lst[middle] < target:
            left = middle + 1
        # If target is smaller, search left half
        else:
            right = middle - 1
    
    # Target not found
    return -1

# Test the function
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Index of 11 in {sorted_list}: {binary_search(sorted_list, 11)}")  # Expected: 5


""" 
Problem 6: Neatly Nested

Understand:
    - What makes a string of parentheses valid?
    - How can we check validity recursively?

Plan:
    - Define base case: empty string is valid
    - For non-empty string:
      - Check if it starts with '(' and ends with ')'
      - If so, recursively check the inner string
      - Also check if it's a concatenation of two valid strings
"""
# Implement
def is_nested(paren_s):
    # Base case: empty string is valid
    if not paren_s:
        return True
    
    # Check if it starts with '(' and ends with ')'
    if paren_s[0] == '(' and paren_s[-1] == ')':
        # Check if inner string is valid
        inner = is_nested(paren_s[1:-1])
        if inner:
            return True
    
    # Try to split the string into two parts
    for i in range(1, len(paren_s)):
        # Check if both parts are valid
        if is_nested(paren_s[:i]) and is_nested(paren_s[i:]):
            return True
    
    return False

# Test the function
print(f"Is '(())' neatly nested? {is_nested('(())')}")  # Expected: True
print(f"Is '()())' neatly nested? {is_nested('()())')}")  # Expected: False


""" 
Problem 7: How Many 1s

Understand:
    - How can we use binary search to count elements?
    - What's the most efficient way to find all 1s in a sorted binary array?

Plan:
    - Use binary search to find the first occurrence of 1
    - Calculate how many 1s are in the list based on the index
    - Return the count
"""
# Implement
def count_ones(lst):
    # Edge cases
    if not lst or lst[-1] == 0:
        return 0
    if lst[0] == 1:
        return len(lst)
    
    # Binary search for first 1
    left = 0
    right = len(lst) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if lst[middle] == 1 and (middle == 0 or lst[middle-1] == 0):
            # Found first 1
            return len(lst) - middle
        elif lst[middle] == 1:
            # Look for earlier 1
            right = middle - 1
        else:
            # Look for 1 to the right
            left = middle + 1
    
    return 0

# Test the function
binary_list = [0, 0, 0, 0, 1, 1, 1]
print(f"Number of 1s in {binary_list}: {count_ones(binary_list)}")  # Expected: 3


""" 
Problem 8: Binary Search IV

Understand:
    - How does a recursive binary search differ from iterative?
    - What are the base and recursive cases?

Plan:
    - Define helper function with left and right pointers
    - Base case: left > right (not found)
    - Calculate middle index
    - Compare and recurse on appropriate half
"""
# Implement
def binary_search_recursive(nums, target):
    # Helper function with pointers
    def binary_search_helper(left, right):
        # Base case: target not found
        if left > right:
            return -1
        
        # Calculate middle index
        middle = (left + right) // 2
        
        # Check if target is at middle
        if nums[middle] == target:
            return middle
        # If target is greater, search right half
        elif nums[middle] < target:
            return binary_search_helper(middle + 1, right)
        # If target is smaller, search left half
            return binary_search_helper(left, middle - 1)
    
    # Start the search
    return binary_search_helper(0, len(nums) - 1)

# Test the function
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Index of 11 in {sorted_list}: {binary_search_recursive(sorted_list, 11)}")  # Expected: 5


""" 
Problem 9: Count Rotations

Understand:
    - What defines a rotation in a circular sorted array?
    - How can we find the pivot point efficiently?

Plan:
    - Use binary search to find the pivot (smallest element)
    - The index of the pivot is equal to the number of rotations
    - Special case: if array is not rotated, return 0
"""
# Implement
def count_rotations(nums):
    # Edge case: empty list or single element
    if not nums or len(nums) == 1:
        return 0
    
    # Initialize pointers
    left = 0
    right = len(nums) - 1
    
    # If first element is smaller than last, array is not rotated
    if nums[left] < nums[right]:
        return 0
    
    # Binary search for pivot
    while left <= right:
        middle = (left + right) // 2
        
        # Check if middle element is pivot
        if middle < len(nums) - 1 and nums[middle] > nums[middle + 1]:
            return middle + 1
        if middle > 0 and nums[middle] < nums[middle - 1]:
            return middle
            
        # Decide which half to search
        if nums[middle] >= nums[0]:
            # Search right half
            left = middle + 1
        else:
            # Search left half
            right = middle - 1
    
    return 0

# Test the function
rotated_list = [8, 9, 10, 2, 5, 6]
print(f"Number of rotations in {rotated_list}: {count_rotations(rotated_list)}")  # Expected: 3


""" 
Problem 10: Merge Sort

Understand:
    - How does merge sort use divide and conquer?
    - What are the steps to implement merge sort recursively?

Plan:
    - Base case: list with 0 or 1 element is already sorted
    - Divide list into two halves
    - Recursively sort each half
    - Merge sorted halves using the helper function
"""
# Implement
def merge(left, right):
    result = []  # List to store the merged result
    i = j = 0    # Pointers to iterate over left and right input arrays
    
    # Compare elements from left and right halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Add any remaining elements from the left half
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add any remaining elements from the right half
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort(lst):
    # Base case: list with 0 or 1 element is already sorted
    if len(lst) <= 1:
        return lst
    
    # Divide list into two halves
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    
    # Merge sorted halves
    return merge(left, right)

# Test the function
unsorted_list = [5, 3, 4, 2, 1]
print(f"Sorted {unsorted_list}: {merge_sort(unsorted_list)}")  # Expected: [1, 2, 3, 4, 5]