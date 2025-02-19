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


