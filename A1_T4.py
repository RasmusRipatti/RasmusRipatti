#Assign value 47 to variable Num1
num1 = 47
#Assign value 102 to a variable Num2
num2 = 102
#Sum variables Num1 and Num2, and put the result into Sum variable
Sum = num1 + num2
#Subtract Num1 from Num2, then store the result in the Diff variable.
Diff = num2 - num1
#Multiply Sum and Diff, then place the resulting product in Product.
Product = Sum * Diff
#Print the sum operation “{Num1} + {Num2} = {Sum}”
print(num1,"+",num2,"=",Sum)
#Print the sub operation “{Num2} - {Num1} = {Diff}”
print(num2,"-",num1,"=",Diff)
#Print the multiply operation “{Sum} * {Diff} = {Product}”
print(Sum,"*",Diff,"=",Product)
#Print the sum, sub and multiply operations together. See “program run” below.
#( 47 + 102 ) * ( 102 - 47 ) = 8195
print("(",num1,"+",num2,")*(",num2,"-",num1,") =",Product)