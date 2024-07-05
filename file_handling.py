
try:
    #user inputs the file name
    input = input('enter the file that you want to sort into vowels and constants: ')
    #open the inputted file in read mode
    f = open(input, 'r')
    #storing all the lists in a list
    lines = f.readlines() 


    #create empty lists to store the vowels and constants
    vowel_list = []
    constant_list = []

    #write the vowels to compare with 
    vowels = 'aeiou'

    #iterate through each item in the list of "lines"
    for line in lines:
        #go through each value of each index whilst removing the \n
        for char in line.strip():
            #if it is a vowel:
            if char in vowels:
                #add to vowels list
                vowel_list.append(char)
            #if isnt vowel but is a letter
            elif char.isalpha():
                #add to constants list
                constant_list.append(char)
    #print the lists
    print('this is the values:', vowel_list)
    print('this is the constants:', constant_list)
except Exception as exception:
    print(exception)
finally:
    f.close()


    




