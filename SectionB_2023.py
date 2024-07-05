def string_validator():
    valid = False
    ascii_sum = 0
    while not valid:
        input_string = input('enter a string to validate: ')
        if 5 <= len(input_string) <= 7:
            if input_string.upper() == input_string:
                if len(set(input_string)) == len(input_string):
                    for i in input_string:
                        ascii_sum += ord(i)
                    if 420 <= ascii_sum <= 600:
                        valid = True
                        return 'this string is valid'
                    else:
                        print('this string is not valid')
                else:
                    print('this string is not valid')
            else:
                print('this string is not valid')
        else:
            print('this string is not valid')

print(string_validator())

