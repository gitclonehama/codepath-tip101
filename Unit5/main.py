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


""" 
Problem 4: Catch Pokemon

Understand:
- How do I add a method to change an attribute?
- What parameters should the method take?

Plan:
- Add a catch method to the Pokemon class
- Demonstrate its use with an example
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
    
    def catch(self):
        self.is_caught = True

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()


""" 
Problem 5: Choose Pokemon

Understand:
- How do I add a conditional method?
- How should the method output be formatted?

Plan:
- Add a choose method to the Pokemon class
- Implement the conditional logic
- Demonstrate with examples
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
    
    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()


""" 
Problem 6: Battle Pokemon

Understand:
- How do I implement a method that affects another object?
- What conditions need to be checked?

Plan:
- Create the Pokemon class with hp and damage
- Implement the attack method with the specified logic
"""
# Implement
class Pokemon():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp # hit points
        self.damage = damage # The amount of damage this pokemon does to its opponent every attack
        
    def attack(self, opponent):
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            opponent.hp = 0
            print(f"{opponent.name} fainted")
        else:
            print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30)

opponent = bulbasaur
pikachu.attack(opponent)


""" 
Problem 7: Convert to Linked List

Understand:
- What is a linked list and how does it differ from a normal list?
- How do I connect nodes together?

Plan:
- Implement the Node class
- Create two nodes with the required values
- Connect them to form a linked list
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node_2 = Node("Wigglytuff")
node_1 = Node("Jigglypuff", node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)


