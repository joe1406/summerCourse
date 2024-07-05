
#pass a list of the string
def recursive_string(str,index):
    #if you reached index 0, stop
    if index == 0:
        return str[index]
    else:
        return str[index] + recursive_string(str, index - 1)

user_string = input('please enter a string: ')
string = list(user_string)
print(recursive_string(string, len(string) - 1))

   
    