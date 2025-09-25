#Make a Python program, which prompts the user name and two floating numbers.
#  Multiply the inserted numbers to get product. Round the product in two decimal precision.
#  Complete the program output as shown below.

print("Program starting")

name = input("What is your name: ")

first_number = input("Enter a floating point number: ")
first_number = float(first_number)

second_number = input("Enter second floating point number: ")
second_number = float(second_number)

print(f"{name} you gave numbers {first_number} and {second_number}")

multi = first_number * second_number
print(f"Multiplying first and second number will result in product {round(multi, 2)}")

print("Program ending")