print("Program starting.")
print("Testing decision structures.")
Value = int(input("Inser an integer: "))


print("Options:")
print("1 - In one multi branched decision")
print("2 - In multiplse independent if statements")
print("0 - Exit")

Choice = int(input("Your choice: "))




if(Choice == 1):
    if(Value >= 400):
        #Value = Value + 44
        Value += 44
    elif(Value >= 200):
        #Value = Value + 22
        Value += 22
    elif(Value >= 100):
        #Value = Value + 11
        Value += 11
    print("Using one multi branched decision structure.")
    print(f"Result is {Value}")
elif(Choice == 2):
    if(Value >= 400):
        Value += 44
    if(Value >= 200):
        Value += 22
    if(Value >= 100):
        Value += 11
    print("Using ")
    print(f"Result is {Value}")
elif(Choice == 0):
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")