###
### Unit 5
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
Problem 1: Pokemon Class

Understand:
- How do I create a class instance in Python?
- What attributes should the Pokemon instance have?

Plan:
- Copy the Pokemon class definition
- Create a new Pokemon instance with name "Pikachu" and type ["Electric"]
"""
# Implement
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

my_pokemon = Pokemon("Pikachu", ["Electric"])


""" 
Problem 2: Create Squirtle

Understand:
- How do I add a method to a class?
- How do I call a method on an instance?

Plan:
- Update the Pokemon class with the print_pokemon method
- Create a Squirtle instance
- Call print_pokemon on the instance
"""
# Implement
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()


""" 
Problem 3: Is Caught

Understand:
- How do I update an attribute of a class instance?
- How can I verify the update worked?

Plan:
- Update squirtle's is_caught attribute to True
- Call print_pokemon to verify the change
"""
# Implement
squirtle.is_caught = True
squirtle.print_pokemon()


