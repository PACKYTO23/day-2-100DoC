# # # Data Types

# # # String

# # # Subscripting
# print("Hello"[4])

# print("123" + "456")

# # # Integer

# print(123 + 456)

# # # Large integers (replacing the comma).
# print(123_456_789)

# # # Float

# pi = 3.14159

# # # Boolean

# x = True
# y = False

# num_char = len(input("What is your name? "))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# # # Type checking
# print(type(new_num_char))

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(70) + str(100))

# / # / # EXERCISE # / # / #

# two_digit_number = input()

# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# / # / # / # / # / #

# print(3 + 5)

# print(7 - 4)

# print(3 * 2)

# # # Always ends up as division.
# print(6 / 3)

# # # Raise a number to a  power.
# print(2 ** 3)

# # # PEMDASLR
# # # Parentheses ()
# # # Exponents **
# # # Multiplication *, Division /
# # # Addition +, Subtraction -

# print(3 * 3 + 3 / 3 - 3)

# print(3 * (3 + (3 / 3) - 3))

# / # / # EXERCISE # / # / #

# height = float(input("Height in m: "))
# weight = int(input("Weight in kg: "))
# BMI = int(weight / (height * height))

# print(BMI)

# / # / # / # / # / #

# # # You decide the number of decimal places.
# print(round(8 / 3, 2))

# # # Floor division without converting into an integer; type: integer.
# print(8 // 3)

# result = 4 / 2
# # # Divides previous value.
# result /= 2
# print(result)

# score = 0
# # # Sums previous value.
# score += 1
# print(score)

# # # f-String

# score = 0
# height = 1.8
# isWinning = True

# print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}.")

# / # / # EXERCISE # / # / #

# age = int(input("Your age: "))

# life_weeks = 90 * 52
# weeks_used = age * 52
# remaining_weeks = life_weeks - weeks_used

# print(f"You have {remaining_weeks} weeks left.")

# / # / # / # / # / #

# / # / # PROJECT OF DAY 2 # / # / #

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
party = int(input("How many people to split the bill? "))
tip = (tip_percentage / 100) + 1

# # # Alternative way:
# bill_to_pay = round(((bill * tip) / party), 2)
bill_to_pay = "{:.2f}".format((bill * tip) / party)

print(f"Each person should pay: ${bill_to_pay}")
