print("Program starting.")
print("")
print("Check multiplicative persistence.")

Num = int(input("Insert an integer: "))

steps = 0

while Num != 0:
    if Num < 10:
        break
    Arvo = int(Num)
    for i in range(Arvo):
        print(i, end=" ")
        if i == len(Num) -1:
            print(" * ")





print("No more steps.")
print("")
print(f"This program took {steps} step(s)")
print("")
print("Program ending.")