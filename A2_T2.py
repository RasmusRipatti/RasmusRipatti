#Make a Python program, which prompts user for a car brand and model. 
# After user inputs, do print the car brand and model sentence with two print commands using “sep” and “end” parameters.



#Example program run:


#Program starting.
print("Program starting")
#Insert car brand: Toyota
Brand = input("Insert car brand: ")
#Insert car model: Corolla
Model = input("Insert car model: ")
#Car brand is "Toyota" and the model is 'Corolla'.
print(f"Car brand is \"{Brand}\" ", end="")
print("and the model is ", f"{Model}'", sep="'")
#Program ending.
print("Program ending.")