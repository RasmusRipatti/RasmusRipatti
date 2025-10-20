#Make Python program which does the following steps:

#Prompt user to insert
#A word
#A character
#Find if the character exists in the word. Possible prints below.
#Word "{WordFirst}" contains character "{Character}"
#Word "{WordFirst}" doesn't contain character "{Character}"
#Prompt user to insert one more word
#Compare the first word to the second word. Examples below:
#The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
#The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
#Both inserted words are the same alphabetically, "{WordFirst}"


#Example program run



#Program starting.
print("Program starting.")
#String comparisons
print("String comparisons")

#Insert first word: beans
Word1 = input("Insert first word: ")
#Insert a character: n
Character = input("Insert a character: ")
#Word "beans" contains character "n"
if(Character in Word1):
    print(f"Word\"{Word1}\"contains character \"{Character}\"")
else:
    print(f"Word \"{Word1}\" doesn't contain character \"{Character}\"")

#Insert second word: banana
Word2 = input("Insert second word: ")
#The second word "banana" is before the first word "beans" alphabetically.
if(Word1 < Word2):
    print(f"The first word \"{Word1}\" is before the second word \"{Word2}\" alphabetically")
elif(Word2 < Word1):
    print(f"The second word \"{Word2}\" is before the first word \"{Word1}\" alphabetically")
else:
    print(f"Both inserted words are the same alphabetically, \"{Word1}\"")

#Program ending.
print("Program ending.")