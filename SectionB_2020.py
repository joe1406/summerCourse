def mode():
    number_of_inputs = int(input("how many numeric digtis would you like to input? "))
    inputs = input(f'enter your {number_of_inputs} inputs: ')
    input_list = list(inputs.replace(' ',''))
    inputs_and_occurences = {}
    for digits in input_list:
        if digits in inputs_and_occurences:
            inputs_and_occurences[digits] += 1
        else:
            inputs_and_occurences[digits] = 1
    maximum_number_of_occurences = max(inputs_and_occurences.values())
    mode = []
    for key in inputs_and_occurences:
        if inputs_and_occurences[key] == maximum_number_of_occurences:
            mode.append(key)
    if len(mode) > 1:
        print('multi-modal')
    else:
        print(f'the mode is {mode[0]}')
    

        
    


mode()