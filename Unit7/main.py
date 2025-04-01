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


