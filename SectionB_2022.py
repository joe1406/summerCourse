def vowel_swap():
    input_string = input("please eneter a string, to swap the vowels: ")
    input_list = list(input_string)
    vowels = 'aeiou'
    vowel_position = []
    vowel_inputs = []
    for i in range(len(input_list)):
        if input_list[i] in vowels:
            vowel_inputs.append(input_string[i])
            vowel_position.append(i)
    reversed_inputs = vowel_inputs[::-1]
    for i in range(len(reversed_inputs)):
        input_list[vowel_position[i]] = reversed_inputs[i]
    return ''.join(input_list)

  
print(vowel_swap())



