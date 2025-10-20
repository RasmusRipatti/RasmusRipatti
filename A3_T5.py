#Create a temperature unit conversion program.

#Start the program by listing options for the user:

#Celsius to Fahrenheit
#Fahrenheit to Celsius
#Exit
#Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.

#For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

#Data representation examples:

#50.0 °F
#10.0 °C
#If the user chooses option Exit, notify the user: Exiting...

#Use 1 decimal precision to round the converted value.


#Example program runs


#Program starting.
print("Program starting.")
#Options:
print("Options:")
#1 - Celsius to Fahrenheit
print("1 - Celsius to Fahrenheit")
#2 - Fahrenheit to Celsius
print("2 - Fahrenheit to Celsius")
#0 - Exit
print("0 - Exit")
#Your choice: 1
Choice = int(input("Your choice: "))

if(Choice == 1):
    Celsius = float(input("Insert the amount of Celsius: "))
    Celsius1 = round(float((Celsius * 1.8) +32), 1)
    print(f"{Celsius} °C equals to {Celsius1} °F")
elif(Choice == 2):
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Fahrenheit1 = round(float((Fahrenheit - 32) / 1.8), 1)
    print(f"{Fahrenheit} °F equals to {Fahrenheit1} °C")
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option.")
#Insert the amount of Celsius: 23
#23.0 °C equals to 73.4 °F

#Program ending.
print("Program ending.")