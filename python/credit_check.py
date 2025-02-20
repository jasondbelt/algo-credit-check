"""
# Credit Check
- The Luhn algorithm is a check-summing algorithm best known for checking the validity of credit card numbers. Write a program that implements the Luhn algorithm to validate a credit card number
- The formula verifies a number against its included check digit, which is usually appended to a partial account number to generate the full account number. This full account number must pass the following test:

* from the rightmost digit, which is the check digit, moving left, double the value of every other digit
* if product of this doubling operation is greater than 9 (e.g., 7 * 2 = 14), then sum the digits of the products (e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5).
* take the sum of all the digits
* if and only if the total modulo 10 is equal to 0 then the number is valid

### Example
We can use the same process to validate an account number. Using `5541808923795240` as our sample input:

```
Account identifier:    5   5   4   1   8   0   8   9   2   3   7   9   5   2   4   0
2x every other digit:  10  5   8   1   16  0   16  9   4   3   14  9   10  2   8   0
Summed digits over 10: 1   5   8   1   7   0   7   9   4   3   5   9   1   2   8   0
Results summed:        1   5   8   1   7   0   7   9   4   3   5   9   1   2   8   0 = 70
```

Since the summed results modulo 10 is zero, the account number is valid according to the algorithm.
"""

"""
Parameter(s): A string of integers
Return: 
- If the string of integers can be validated with Luhn Algorithm, 
  - return str: "The number is valid!"
- If the string of integers can't be validated:
  - return str: "The number is invalid!"
Example(s) Plenty down below to test, but really just focused on the main one that was already broken down.
Pseudocode within the funttion
"""
# individual function used for third calculation (can't use within credit check function)
sum_of_digits = lambda n: sum(int(digit) for digit in str(n))

def credit_check(str):
# Convert input string of numbers to a list of integers.
    first_calc = [int(x) for x in str]
    
# Loop through first calc and double each number if it's at an even index
    second_calc = [num * 2 if i % 2 == 0 else num for i, num in enumerate(first_calc)]

# Loop through each number, use sum_of digits function sum up the individual digits
# for each number, really only ends up changing double digit numbers, like 10 = 1+0
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
