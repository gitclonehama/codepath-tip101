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

print_menu("🍕")  # Change this to your lunch choice


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

result = sum(13, 27)
print(result * 2)


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

print(product(22, 7))


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


