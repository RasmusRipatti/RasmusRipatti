print("Program starting.")

Num = int(input("Insert a positive integer: "))
stop = 1
steps = 0


while Num != stop:
    Result = round(Num)
    print(Result, end=" -> ")
    steps += 1
    if(Num%2 == 0):
        Num = Num/2
    elif(Num%2 == 1):
        Num = Num*3+1
if Num == stop:
    print("1")



print(f"Sequence had {steps} total steps.")
print("")
print("Program ending.")
