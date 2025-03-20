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


