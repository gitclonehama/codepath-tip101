###
### Unit 5
###


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


""" 
Problem 8: Add First

Understand:
- How do I insert a new node at the beginning of a linked list?
- What should be returned from the function?

Plan:
- Set the next pointer of the new node to the current head
- Return the new node as the new head
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def add_first(head, new_node):
    new_node.next = head
    return new_node

# Using the Linked List from Problem 7
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)


""" 
Problem 9: Get Tail

Understand:
- How do I traverse a linked list to find the tail?
- How do I handle edge cases like an empty list?

Plan:
- Check if the head is None and return None if it is
- Traverse the list until finding a node with next = None
- Return that node's value
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_tail(head):
    if head is None:
        return None
    
    current = head
    while current.next is not None:
        current = current.next
        
    return current.value

# Example usage
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)
# linked list: num1->num2->num3

head = num1
tail = get_tail(head)
print(tail)


""" 
Problem 10: Replace Node

Understand:
- How do I traverse a linked list and update values?
- Do I need to handle edge cases?

Plan:
- Traverse the linked list
- For each node, check if its value matches the original value
- If it does, update it to the replacement value
"""
# Implement
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def ll_replace(head, original, replacement):
    current = head
    while current is not None:
        if current.value == original:
            current.value = replacement
        current = current.next

# Example usage
num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")

# Print the updated linked list
current = head
while current is not None:
    print(current.value, end="")
    if current.next is not None:
        print(" -> ", end="")
    current = current.next