

print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
Choice1 = int(input("Your choice: "))

if(Choice1 == 1):
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Choice1_1 = int(input("Your choice: "))
    if(Choice1_1 == 1):
        Meters = float(input("Insert meters: "))
        Meters1 = round(float(Meters / 1000), 1)
        print(f"{Meters} m is {Meters1} km")
    elif(Choice1_1 == 2):
        Km = float(input("Insert Kilometers: "))
        Km1 = round(float(Km * 1000), 1)
        print(f"{Km} km is {Km1} m")
    elif(Choice1_1 == 0):
        print("Exiting...")
    else:
        print("Unknown option.")
elif(Choice1 == 2):
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Choice1_2 = int(input("Your choice: "))
    if(Choice1_2 == 1):
        Grams = float(input("Insert grams: "))
        g = round(float(Grams / 453.59237), 1)
        print(f"{Grams} g is {g} lb")
    elif(Choice1_2 == 2):
        Pounds = float(input("Insert pounds: "))
        lb = round(float(Pounds * 453.59237), 1)
        print(f"{Pounds} lb is {lb} g")
    elif(Choice1_2 == 0):
        print("Exiting...")
    else:
        print("Unknown option.")
elif(Choice1 == 0):
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")