"""
# Credit Check
Parameter(s): A string of integers
Return: 
- If the string of integers can be validated with Luhn Algorithm, 
  - return str: "The number is valid!"
- If the string of integers can't be validated:
  - return str: "The number is invalid!"
Example(s) Plenty down below to test, but really just focused on the main one that was already broken down.
Pseudocode within the function

1. List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

2. https://www.w3schools.com/python/python_lists_comprehension.asp
"""
# individual function used for third calculation (can't use within credit check function)
sum_of_digits = lambda n: sum(int(digit) for digit in str(n))

def credit_check(str):
# Convert input string of numbers to a list of integers.
    first_calc = [int(x) for x in str]
    
# Loop through first calc and double each number if it's at an even index
    second_calc = [num * 2 if i % 2 == 0 else num for i, num in enumerate(first_calc)]

# Loop through each number, use sum_of digits function on each number in second_calc list, really only ends up changing double digit numbers, like 10 = 1+0
    third_calc = [sum_of_digits(x) for x in second_calc]
   
# ternary statement
# sum up digits in third calc. If the sum is modulo 10 is 0, return True, else false
    return "The number is valid!" if sum(third_calc) % 10 == 0 else "The number is invalid!"

print(credit_check('5541808923795240') == "The number is valid!")
print(credit_check("4024007136512380") == "The number is valid!")
print(credit_check("6011797668867828") == "The number is valid!")

print(credit_check("5541801923795240") == "The number is invalid!")
print(credit_check("4024007106512380") == "The number is invalid!")
print(credit_check("6011797668868728") == "The number is invalid!")