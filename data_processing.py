#Prompt the user to enter a sentence and then print the sentence in uppercase letters.
#Prompt the user to enter a paragraph and then count the number of words in the paragraph.
#Prompt the user for a string, and check if all the characters in the string are digits. Output true or false
#Prompt the user for a string, and replace all occurrences of the letter "a" with the letter "o".
#Prompt the user to enter their full name and then print their initials. Assume that the user will enter their full name with a space between each name.
#Prompt the user for a string, then print its length.

sentence = input("please enter a sentence: ").upper()
print(f"in uppercase, your sentence is: {sentence}")

paragraph = input("enter a paragraph: ").strip().split()
print(len(paragraph))

string = input("enter a string: ").isdigit()
print(string)

string_replace = input("enter a string: ").lower().replace("a","o")
print(string_replace)

full_name = input("enter your full name: ").title().split()
initals = []
for name in full_name:
    initals.append(name[0])
print("".join(initals))

final_string = input("enter a string: ").strip().replace(" ","")
print(len(final_string))

