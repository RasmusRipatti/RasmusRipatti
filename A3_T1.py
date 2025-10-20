#Make Python program and implement if-statements in proper places.

#Ask user to insert two integers
#Compare the integers and then announce the greater number
#Create sum of the two integers
#Check the parity of the sum (see modulo-operator ‘%’)
#Other possible output variants:

#Integer comparison
#Integers are the same.
#First integer is greater.
#Parity check
#Sum is even.


#Example program run


#run 1 run 2 run 3

#Program starting.
print("Program starting.")
#Insert two integers.
print("Insert two integers.")
#Insert first integer: 5
Num1 = int(input("Insert first integer: "))
#Insert second integer: 5
Num2 = int(input("Insert second integer: "))
#Comparing inserted integers.
print("Comparing inserted integers.")
#Integers are the same
if(Num1 == Num2):
    print("Integers are the same")
elif(Num1 > Num2):
    print("First integer is greater")
else:
    print("Second integer is greater")

#Adding integers together
print("Adding integers together")
#5 + 5 = 10
Sum = Num1 + Num2
print("",Num1, "+", Num2, "=", Sum,)

#Checking the parity of the sum...
print("Checking the rarity of the sum...")
#Sum is even.
if(Sum % 2 == 0):
    print("Sum is even.")
else:
    print("Sum is odd")
#Program ending.
print("Program ending.")