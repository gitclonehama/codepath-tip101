###
### Unit 2
###


""" 
Problem 1: Subsequence


Understand:
    - input parameters lst (list of ints), sequence (list of ints)
    - goal: determine if 'sequence' is a subsequence of 'lst'
    - subsequence => set of numbers that appear in same relative order (not necessarily adjacent)
    - True if sequence exists, False otherwise

Plan:
    - have a pointer for sequence and lst
    - loop through lst, incremting both pointers if they match
    - after the loop is done, if we exhausted sequence, then return True
    - if we are not at the end of sequence, return false

"""
# Implement

def is_subsequence(lst, sequence):
    seq_idx = 0

    for i in range(len(lst)):

        if seq_idx >= len(sequence):
            return True

        if lst[i] == sequence[seq_idx]:
            seq_idx += 1
    
    return False

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))    # Expected: True

""" 
Problem 2:


Understand:


Plan:


"""
# Implement


""" 
Problem 3:


Understand:


Plan:


"""
# Implement


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
