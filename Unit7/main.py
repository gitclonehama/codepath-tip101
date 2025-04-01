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


