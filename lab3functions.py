"""

def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(10))

"""
"""

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

print(fahrenheit_to_celsius(98.6))

"""
"""

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None


print(solve(35, 94))

"""

"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

nums = [1, 2, 3, 4, 5, 11, 15, 17, 20]
print(filter_prime(nums)) 

"""


"""
import itertools

def print_permutations(s):
    perms = itertools.permutations(s)
    for p in perms:
        print("".join(p))


print_permutations("abc")

"""

"""

def reverse_sentence(s):
    words = s.split()
    return " ".join(words[::-1])

print(reverse_sentence("We are ready"))

"""

"""

def has_33(nums):
    for i in range(len(nums) - 1):          
        if nums[i] == 3 and nums[i+1] == 3: 
            return True
    return False

# Tests
print(has_33([1, 3, 3]))      
print(has_33([1, 3, 1, 3]))   
print(has_33([3, 1, 3]))

"""

"""

def spy_game(nums):
    code = [0, 0, 7]   
    for n in nums:
        if n == code[0]:   
            code.pop(0)    
        if not code:       
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))  
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  


"""

"""

import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)


print(sphere_volume(3)) 

"""

"""

def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


print(unique_list([1,2,2,3,4,4,5]))

"""

"""

def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1]


print(is_palindrome("madam"))          
print(is_palindrome("nurses run"))     
print(is_palindrome("hello")) 

"""

"""

def histogram(nums):
    for n in nums:
        print('*' * n)

histogram([4, 9, 7])

"""

"""

import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number = random.randint(1, 20)   # secret number
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())         # user input
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()

"""
