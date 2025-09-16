#Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) and present the consumption in liters per 100km “x l per 100 km”


#Print info message “Calculate fuel consumtion.”
print("Calculate fuek consumption.")
#Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
num1 = int(input("Enter travel distance(kilometers): "))
#Convert the Feed into an integer and assign it to Distance variable
Distance = num1
#Ask “Enter fuel usage(liters): ”
num2 = int(input("Enter fuel usage(liters): "))
#Convert the Feed into an integer and assign it to FuelUsage variable
FuelUsage = num2
#Calculate the Consumption for 100 km
Consumption = FuelUsage/Distance*100
#Convert the Consumption back to an integer

#Print “Fuel consumption is {Consumption} l per 100 km”
print("Fuel consumption is",Consumption,"l per 100 km")