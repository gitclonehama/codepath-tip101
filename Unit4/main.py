###
### Unit 4
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
Problem 1: Prime Number

Write a function is_prime() that takes in a positive integer n and returns True if it is a prime 
number and False otherwise. A prime number is a number greater than 1 that has no positive 
divisors other than 1 and itself.

Understand:
    - Do I need to handle edge cases like n <= 1?
    - What's the most efficient way to check for primality?

Plan:
    - If n <= 1, return False (not prime by definition)
    - If n is 2, return True (the only even prime)
    - If n is divisible by 2, return False (even numbers > 2 aren't prime)
    - Check divisibility for all odd numbers from 3 to sqrt(n)
    - If no divisors found, return True

"""
# Implement
def is_prime(n):
    # Handle edge cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check all odd numbers from 3 to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

# Test the function
print(is_prime(5))  # True
print(is_prime(12))  # False
print(is_prime(9))  # False


""" 
Problem 2: Two-Pointer Reverse List

Write a function reverse_list() that takes in a list lst and returns elements of the list in 
reverse order. The list should be reversed in-place without using list slicing.

Understand:
    - What does it mean to reverse in-place?
    - How can I use the two-pointer technique for this problem?

Plan:
    - Initialize two pointers: left at the beginning and right at the end
    - While left < right:
        - Swap the elements at left and right indices
        - Increment left and decrement right
    - Return the modified list

"""
# Implement
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        # Swap elements
        lst[left], lst[right] = lst[right], lst[left]
        
        # Move pointers inward
        left += 1
        right -= 1
    
    return lst

# Test the function
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]


""" 
Problem 3: Evaluating Solutions

The reverse_list() problem can also be solved without using the two pointer technique. 
Evaluate the time and space complexity of the two-pointer solution vs. the slice solution.

Understand:
    - How do we analyze time complexity for each solution?
    - How do we analyze space complexity for each solution?

Plan:
    - Compare the two-pointer approach with the slice approach
    - Analyze operations and memory usage for both

"""
# Implement
"""
Two-Pointer Solution Analysis:
Time Complexity: O(n) - we process each element once
Space Complexity: O(1) - we only use a constant amount of extra space

Slice Solution Analysis:
def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]
        
Time Complexity: O(n) - we process each element twice (once for slicing, once for copying)
Space Complexity: O(n) - we create a new list of the same size

Comparison:
- Time Complexity: Both are O(n), but the two-pointer approach has fewer operations
- Space Complexity: Two-pointer is better with O(1) vs O(n) for the slice approach

The two-pointer technique is more efficient in terms of space complexity.
"""


""" 
Problem 4: Move Even Integers

Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even 
integers at the beginning of the list followed by all the odd integers.

Understand:
    - Do we need to maintain the original relative order within even and odd groups?
    - Does the function modify the original list or return a new one?

Plan:
    - Use two pointers approach
    - Start with left at the beginning of the list
    - For each element, check if it's even
    - If even, swap with the element at left pointer and increment left
    - Return the modified list

"""
# Implement
def sort_array_by_parity(nums):
    left = 0
    
    for i in range(len(nums)):
        if nums[i] % 2 == 0:  # If current number is even
            # Swap with the position at left pointer
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
    
    return nums

# Test the function
print(sort_array_by_parity([3, 1, 2, 4]))  # [2, 4, 3, 1] or similar with evens first
print(sort_array_by_parity([0]))  # [0]


""" 
Problem 5: Palindrome

Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the 
first palindromic string in the list.

Understand:
    - What defines a palindrome? Does it read the same forward and backward?
    - What should we return if no palindrome is found in the list?

Plan:
    - Create a helper function to check if a string is a palindrome
    - Iterate through the list of words
    - For each word, check if it's a palindrome using our helper function
    - Return the first palindrome found, or "" if none exists

"""
# Implement
def is_palindrome_string(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def first_palindrome(words):
    for word in words:
        if is_palindrome_string(word):
            return word
    return ""

# Test the function
words = ["abc", "car", "ada", "racecar", "cool"]
print(first_palindrome(words))  # "ada"

words2 = ["abc", "racecar", "cool"]
print(first_palindrome(words2))  # "racecar"

words3 = ["abc", "def", "ghi"]
print(first_palindrome(words3))  # ""


""" 
Problem 6: Remove Duplicates with O(1)

Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and 
removes the duplicates in-place such that each element appears only once.

Understand:
    - How do we handle an empty list?
    - Can we modify the original list? What should the final state be?

Plan:
    - Use two pointers: one for the position to place the next unique element (unique_pos)
    - Iterate through the list starting from the second element
    - If current element != previous unique element, place it at unique_pos and increment unique_pos
    - Return the count of unique elements
    - The list will be modified in-place with unique elements at the start

"""
# Implement
def remove_duplicates(nums):
    if not nums:
        return 0
        
    unique_pos = 1  # Position to place the next unique element
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[unique_pos] = nums[i]
            unique_pos += 1
    
    # Truncate the list to only include unique elements
    return unique_pos

# Test the function
nums = [1, 1, 2, 3, 4, 4, 4, 5]
print(nums)
print(remove_duplicates(nums))
print(nums)  # First 5 elements will be [1, 2, 3, 4, 5]


""" 
Problem 7: Perfect Number

Write a function is_perfect_number() that takes in a positive integer n and returns True if it is a perfect 
number and False otherwise. A perfect number is a positive integer that equals the sum of its proper divisors.

Understand:
    - What are proper divisors? (Numbers that divide evenly excluding the number itself)
    - What's the most efficient way to find all proper divisors?

Plan:
    - Initialize sum_of_divisors to 1 (1 is always a proper divisor)
    - Check all numbers from 2 to sqrt(n):
        - If n is divisible by i, add both i and n/i to the sum
    - Return True if sum_of_divisors equals n, False otherwise

"""
# Implement
def is_perfect_number(n):
    if n <= 1:
        return False
    
    sum_of_divisors = 1  # Start with 1 as it's always a proper divisor
    
    # Check divisors up to sqrt(n)
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_of_divisors += i
            if i != n // i:  # Avoid adding the same divisor twice (for perfect squares)
                sum_of_divisors += n // i
        i += 1
    
    return sum_of_divisors == n

# Test the function
print(is_perfect_number(6))   # True (1+2+3=6)
print(is_perfect_number(28))  # True (1+2+4+7+14=28)
print(is_perfect_number(9))   # False (1+3=4≠9)


""" 
Problem 8: 2-Pointer Palindrome

Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is 
a palindrome and False otherwise. Use the two-pointer technique.

Understand:
    - Are we only considering lowercase alphabetic characters?
    - Do we need to handle empty strings or single character strings?

Plan:
    - Initialize two pointers: left at beginning and right at end
    - While left < right:
        - If characters at left and right are different, return False
        - Increment left, decrement right
    - Return True if we complete the loop

"""
# Implement
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test the function
s1 = "amanaplanacanalpanama"
s2 = "helloworld"
print(is_palindrome(s1))  # True
print(is_palindrome(s2))  # False


""" 
Problem 9: Evaluate Palindrome

Compare the time and space complexity of the two-pointer approach vs. the slice approach for palindrome checking.

Understand:
    - What operations are performed in each approach?
    - How much extra memory is used in each approach?

Plan:
    - Analyze the two-pointer approach
    - Compare with the slice approach

"""
# Implement
"""
Two-Pointer Approach Analysis:
Time Complexity: O(n) - we check at most n/2 character pairs
Space Complexity: O(1) - we only use two pointers regardless of input size

Slice Approach Analysis:
def is_palindrome(s):
    reverse = s[::-1]
    return reverse == s

Time Complexity: O(n) - creating the reversed string takes O(n) time
Space Complexity: O(n) - we create a new string of the same length

Comparison:
- Time Complexity: Both are O(n), but two-pointer has fewer operations
- Space Complexity: Two-pointer is better with O(1) vs O(n)

The two-pointer approach is more efficient in terms of space complexity.
"""


""" 
Problem 10: Make Palindromes

Write a function make_palindrome() that turns a string into a palindrome with the minimum 
number of operations, making the lexicographically smallest one if there are multiple options.

Understand:
    - What is a lexicographically smaller string?
    - How do we determine the minimum number of operations?

Plan:
    - Use two pointers approach to identify mismatches
    - For each mismatch, choose the lexicographically smaller character
    - Build the palindrome by making the minimum changes

"""
# Implement
def make_palindrome(s):
    s_list = list(s)
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s_list[left] != s_list[right]:
            # Choose the lexicographically smaller character
            if s_list[left] < s_list[right]:
                s_list[right] = s_list[left]
            else:
                s_list[left] = s_list[right]
        left += 1
        right -= 1
    
    return "".join(s_list)

# Test the function
print(make_palindrome("egcfe"))  # efcfe
print(make_palindrome("abcd"))   # abba
print(make_palindrome("seven"))  # neven