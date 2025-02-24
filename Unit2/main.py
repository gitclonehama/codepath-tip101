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
    for item, amount in restock_list.items():
        # Check if item exists
        existing = current_inventory.get(item)
        if existing:
            # If item exists, increment its stock
            current_inventory[item] += amount
        else:
            # Item doesn't exist, so create and set amount to be restock value
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
print('''Expected:
{"apples": 40,"bananas": 15,"oranges": 30,"pears": 5}''')



""" 
Problem 6: Cast Vote


Understand:
    - Funtion Records a voote for a candidate in an election
    - Param:
        votes: dict that maps candidates to their current number of votes
        candidate: represents the candidate the user would like to vote for
                    if not exist, add them to the dictionary
    - return the updated dictionary

Plan:
    - Go through votes
    - check if string exists in votes
    - if not, add it to dict and set value as 1 (their first vote)
    - if it does, increment the value of key "candidate"
    - return the updated dict

"""
# Implement
def cast_vote(votes: dict, candidate: str):
    # check if candidate exists in votes dict
    existing = votes.get(candidate)

    if existing:
        # Candidate exists in votes, increment votes
        votes[candidate] += 1
    else:
        # Candidate does not exist in votes, so we create it and cast first vote
        votes[candidate] = 1

    # Return the updated dict
    return votes

print("\nTesting Problem 6")
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

print('''\nExpected:
{"Alice": 6, "Bob": 3}
{"Alice": 6, "Bob": 3, "Gina": 1}
''')


""" 
Problem 7: Keys in Common


Understand:
    - Given dict1, and dict2, find all keys common, return a list of all common keys

Plan:
    - unpack all keys in dict1
    - int he loop, check if the key exists in dict2
    - if it exists, append key to result list
    - return result list comprised of all common keys

"""
# Implement
def common_keys(dict1: dict, dict2: dict):
    # Result list to append common keys
    result = []

    # Go through all the keys in dict1
    for key in dict1.keys():
        # Check if key exists in dict2
        if dict2.get(key):
            # Key exists, so append it to result
            result.append(key)

    # Once the loop is done, result should hold all common keys, return it
    return result

# Testing:
print("\nTesting Problem 7")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

print('''\nExpected:
['b', 'c']
''')


""" 
Problem 8: Highest Priority Task


Understand:
    - Given a dictionary tasks where keys are task names and values are int priorities
    - removes the highest priority task from the dictionary and returns its name
    - in case of multiple tasks with same prio, return first based alphabatically

Plan:
    - loop through dictoionary and unpack
    - keep track of highest priority
    - check if priority ==, check name for alphabat for tie breaker
    - pop the task from the dict, return the key
"""
# Implement
def get_highest_priority_task(tasks: dict):
    # Loop through and unpack key, value from tasks
    currTask = ""
    currPrio = 0
    for task, priority in tasks.items():
        # Compare current highest to priority, save if current task is higher
        if priority > currPrio:
            # New highest prio, save prio and task
            currPrio = priority
            currTask = task
        elif priority == currPrio:
            # Equal prio case, switch if task < alphabetically
            currTask = task if task < currTask else currTask
    
    # Once done with loop, currTask is the task we want to pop
    tasks.pop(currTask)
    
    # Return the name of the task that got removed
    return currTask

# Testing
print("Testing Problem 8")
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)

print('''\nExpected:
task2
task4
task3
{"task1": 8, "task5": 7}
''')


""" 
Problem 9: Frequency Count


Understand:
    - A functioon that takes in list of ints (nums) and counts the occurances
    - Return ints as keys and their occurances as values

Plan:
    - Create result dict
    - Loop through the list of nums
    - if nums exists in dict, increment occurance
    - if not, create in dict and assign 1 (first occurance)
    - return the result dict

"""
# Implement
def count_occurrences(nums: list[int]):
    # Create result dict
    result = dict()

    # Loop through nums
    for num in nums:
        # Check if num exists in result dict
        if result.get(num):
            # num exists, increment it's value
            result[num] += 1
        else:
            # num does not exist, create and set value = 1
            result[num] = 1
    
    # Once loop is done, result is complete, return it
    return result

# Testing
print("Testing problem 9")
nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))

print('''\nExpected:
{1: 1, 2: 2, 3: 3, 4: 1}
''')



""" 
Problem 10: Find Majority Element


Understand:
    - Take in a list of ints (elements) and find the majority element in the list
    - Majority element = element that appears more than n/2 times *if n = len(elements)
    - If no clear majority element, return None
    - Using boyer moore algorithm
Plan:
    - Keep track of current element
    - Loop through the list
    - everytime we encounter an element that matches, increase the value of current element
    - if its different, decrement
    - check if the count is > n/2

"""
# Implement
def find_majority_element(elements: list[int]):

    # Keep track of current elements (set to first element) and count
    current = elements[0]
    count = 1

    # Loop through elements (starting index 1)
    for element in elements[1:]:
        
        # Check if count is 0
        if count == 0:
            # Our base case, we assign new element and set count to 1
            current = element
            count = 1
        elif element == current:
            # Match, increment count
            count += 1
        else:
            # No match, decrement count
            count -= 1

    # End of loop, check if count is > n/2:
    verified_count = sum(1 for element in elements if element == current)
    return current if verified_count > len(elements)//2 else None

# Testing:
print("\nTesting problem 10")
elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))
print('''Expected:
2
''')