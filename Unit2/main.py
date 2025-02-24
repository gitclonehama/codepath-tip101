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
Problem 4:


Understand:


Plan:


"""
# Implement


""" 
Problem 5:


Understand:


Plan:


"""
# Implement


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
