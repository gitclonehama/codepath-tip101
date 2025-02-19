###
### Unit 1
###


"""
Problem 1: Hello World!

Understand:
    - What is the correct order to define and call a function within Python?
    - How do we get a message to print inside a function?

Plan:
    - Define a function hello_world() that 
    - Use print() with the string "Hello world!" inside it
    - Call the function
"""

# Implement:
def hello_world():
    print("Hello world!")

hello_world()


"""
Problem 2: Today's Mood

Understand:
    - How can we modify a variable inside a function?
    - How can we print a message that includes a variable?

Plan:
    - Define a function `todays_mood()` that sets a mood variable
    - Print "Today's mood: " followed by the mood
    - Call the function
"""

# Implement:
def todays_mood():
    mood = "🥱"  # Change this to reflect today's mood
    print("Today's mood: " + mood)

todays_mood()


"""
Problem 3: Lunch Menu

Understand:
    - How do we pass a parameter to a function?
    - How do we print a formatted message with an argument?

Plan:
    - Define a function `print_menu(menu)`
    - Print "Lunch today is: " followed by the menu
    - Call the function with an argument
"""

# Implement:
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu("🍜")  # Change this to your lunch choice


"""
Problem 4: Sum of Two Integers

Understand:
    - How do we return the sum of two numbers?
    - How do we double the result and print it?

Plan:
    - Define a function `sum(a, b)` that returns the sum
    - Call the function with (13, 27)
    - Multiply the result by 2 and print it
"""

# Implement:
def sum(a, b):
    return a + b

result = sum(20, 8)
print(result * 2)   # Output 56


"""
Problem 5: Product of Two Integers

Understand:
    - How do we return the product of two numbers?
    - How do we print the result?

Plan:
    - Define a function `product(a, b)` that returns the product
    - Call the function with (22, 7) and print the result
"""

# Implement:
def product(a, b):
    return a * b

print(product(22, 7))   # Ouput: 154


"""
Problem 6: Print List Items

Understand:
    - How do we iterate through items in a list?
    - How do we print each item on a new line?

Plan:
    - Define a function `print_list(lst)` that takes a list parameter
    - Loop through each item in the list
    - Print each item
"""

# Implement:
def print_list(lst):
    for item in lst:
        print(item)

# Test the function
test_list = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(test_list)


"""
Problem 7: Double List Values

Understand:
    - How do we modify each number in a list?
    - How do we return a new list with modified values?

Plan:
    - Define a function `doubled(lst)` that takes a list parameter
    - Create a new list with doubled values
    - Return the new list
"""

# Implement:
def doubled(lst):
    return [num * 2 for num in lst]

# Test the function
numbers = [1, 2, 3]
print(doubled(numbers))


"""
Problem 8: Flip Number Signs

Understand:
    - How do we change the sign of a number?
    - How do we create a new list with modified values?

Plan:
    - Define a function `flip_sign(lst)` that takes a list parameter
    - Create a new list with flipped signs
    - Return the new list
"""

# Implement:
def flip_sign(lst):
    return [-num for num in lst]

# Test the function
numbers = [1, -2, -3, 4]
print(flip_sign(numbers))


"""
Problem 9: Maximum Difference

Understand:
    - How do we find the min and max values in a list?
    - How do we calculate the difference between two numbers?

Plan:
    - Define a function `max_difference(lst)` that takes a list parameter
    - Find the minimum and maximum values
    - Return their difference
"""

# Implement:
def max_difference(lst):
    return max(lst) - min(lst)

# Test the function
numbers = [5, 22, 8, 10, 2]
print(max_difference(numbers))


"""
Problem 10: List Statistics

Understand:
    - How do we calculate the average of a list?
    - How do we return multiple values from a function?

Plan:
    - Define a function `list_stats(lst)` that takes a list parameter
    - Calculate the sum, average, and length of the list
    - Return all three values as a tuple
"""

# Implement:
def list_stats(lst):
    total = sum(lst)
    length = len(lst)
    average = total / length
    return (total, average, length)

# Test the function
numbers = [1, 2, 3, 4, 5]
total, avg, length = list_stats(numbers)
print(f"Sum: {total}, Average: {avg}, Length: {length}")
