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


