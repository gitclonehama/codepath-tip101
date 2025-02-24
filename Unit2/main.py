###
### Unit 2
###


""" 
Problem 1: Subsequence

Understand:
    - What inputs does the function need to handle?
    - What defines a valid subsequence?

Plan:
    - Define function that takes lst and sequence parameters
    - Track position in sequence while iterating through lst
    - Return True if sequence is found, False otherwise
"""

# Implement
def is_subsequence(lst, sequence):
    # Keep track of where we are in sequence
    seq_idx = 0

    # Loop through the list
    for num in lst:
        # If there is a match to what we are pointing at in sequence
        if num == sequence[seq_idx]:
            # Look at next number
            seq_idx += 1
            # We must've matched all entries in sequence if idx is pointing one past it
            if seq_idx == (len(sequence)):
                return True
    
    return False

# Test the function
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))    # Expected: True

lst2 = [5, 1, 22, 25, -1, 6, 8, 10]
sequence2 = [1, 6, -1, 10]
print(is_subsequence(lst2, sequence2))    # Expected: False

lst3 = [5, -1, 1, 22, -1, 25, 8, 6, 10, -1, 10]
sequence3 = [1, 6, -1, 10]
print(is_subsequence(lst3, sequence3))    # Expected: True


""" 
Problem 2: Create a Dictionary


Understand:
    - What happens if you have different list lenghths?
    - Are there any edge cases?

Plan:
    - Loop through range length of keys
    - Assign a value to them at the same index
    - Return the dictionary

"""
# Implement
def create_dictionary(keys, values):
    result = dict()

    # Loop through range of keys list len
    for i in range(len(keys)):
        # Add pair of key: value from the list for each i
        result[keys[i]] = values[i]

    return result

# Testing:
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print("Result:  ", create_dictionary(keys, values))  
print('Expected: {"peanut": "butter", "dragon": "fly", "star": "fish", "pop": "corn", "space": "ship"}')


"""
Problem 3: Print Pair


Understand:
    - Inputs dictionary and a key 'target'
    - Looks for target, when found, prints key and value
    - Format:   Key : <key>
                Value: <value>

Plan:
    - Use the get method and print the result if found
    - If get returns with error, print "That pair does not exist!"

"""
# Implement
def print_pair(dictionary : dict, target):
    value = dictionary.get(target)

    if value == None:
        print("That pair does not exist!")
    else:
        print(f'Key: {target}\nValue: {value}')

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print("\nResult:")
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

print("""
Expected:
Key: patrick
Value: star
That pair does not exist!
Key: spongebob
Value: squarepants""")


""" 
Problem 4: Keys Versus Values


Understand:
    - takes in a dictionary of key: value ints
    - find sum of all keys, sum of all values
    - return the name of the group that has higher sum

Plan:
    - loop through dictionary using .items()
    - add up all values into seperate groups
    - after done with loop, compare sums and announce winner
"""
# Implement
def keys_v_values(dictionary: dict):
    # Keep track of sums seperately
    keySum = 0
    valSum = 0

    # Unpack the dictionary keys and values
    for key, val in dictionary.items():
        keySum += key
        valSum =+ val

    # Out of loop, compare and print
    if keySum == valSum:
        return("balanced")
    elif keySum > valSum:
        return("keys")
    else:
        return("values")

# Testing:
print("\nTests Problem 4")
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)
print("""
Expected:
values
keys
""")

""" 
Problem 5: Restock Inventory


Understand:
    - Updates an inventory dict based on restock list
    - 2 params: 
        current_inventory: dict where each key-value pair represents item and current stock
        restock_list: dict where each key-value pair represents item and quantity to be added to stock
    - If an item in restock_list is not in current_inv, it should be added
    - return current_inventory with the updates

Plan:
    - Loop through restock, keep track of items
    - use get(item) on current_inventory
    - if item exists, (not None) then increment stock by restock amount
    - if not, create key and set its value to be restock amount
    - return updated dict
"""
# Implement
def restock_inventory(current_inventory: dict, restock_list: dict):
    # Unpack restock_list
    for item, amount in restock_list.values():
        # Check if item exists
        existing = current_inventory.get(item)
        # If item exists, increment its stock
        if existing:
            current_inventory[existing] += amount
        # Item doesn't exist, so create and set amount to be restock value
        else:
            current_inventory[item] = amount
    
    # Return the updated dict
    return current_inventory

# Testing:
print("Tests Problem 5")
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}
restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory, restock_list))
print('Expected: current_inventory = {"apples": 40,"bananas": 15,"oranges": 30,"pears": 5}')



""" 
Problem 6:


Understand:


Plan:


"""
# Implement


""" 
Problem 7:


Understand:


Plan:


"""
# Implement


""" 
Problem 8:


Understand:


Plan:


"""
# Implement


""" 
Problem 9:


Understand:


Plan:


"""
# Implement


""" 
Problem 10:


Understand:


Plan:


"""
# Implement
