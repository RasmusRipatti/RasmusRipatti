#Write a Python program which asks user to insert hex color. 
# In this case hex color is expected to be the 7 character representation starting with # and followed by 6 0-F characters to represent RGB colors. 
# More about hex colors at https://en.wikipedia.org/wiki/Web_colors


#Slice the amount of red, green and blue from that inserted color and display each color as shown below.


#Example program run:


#Program starting.
print("Program starting.")
#Insert a hex color: #FFA500
Hex_color = input("Insert a hex color: ")

#Colors
print("Colors")
#- Red FF
print(f"- Red {Hex_color[1:3:1]}")
#- Green A5
print(f"- Green {Hex_color[3:5:1]}")
#- Blue 00
print(f"- Blue {Hex_color[5:7:1]}")

#Program ending.
print("Program ending.")