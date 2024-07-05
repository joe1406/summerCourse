# Write a program that asks the user to enter a string. It should then change the order
# of the vowels in the string and display the result.
# If there are n vowels in the string, the 1st vowel in the string should swap with the nth vowel in the string, the 2nd vowel in the string should swap with the (n-1)th vowel in the string, and so on.
# # The letters a, e, i, o and u are the only vowels.

# # Examples
# # If the user enters the string horse then the program should display the string herso.
# # If the user enters the string goose then the program should display the string geoso.

def vowel_swap(string):
    vowels = "aeiou"
    string_list = list(string)
    vowel_indices = []
    vowel_chars = []
    for i in range(len(string_list)):
        if string_list[i] in vowels:
            vowel_indices.append(i)
            vowel_chars.append(string_list[i])
    reversed_vowels = vowel_chars[::-1]
    for i in range(len(vowel_indices)):
        string_list[vowel_indices[i]] = reversed_vowels[i]
    return ''.join(string_list)

input_str = input("Please enter a string: ")

print(vowel_swap(input_str))





            
    




