def run_length_encoding(string):
    str_list = list(string)
    str_list.append('')
    counter = 1
    output = []
    for i in range(0,len(str_list)-1):
        if str_list[i] == str_list[i+1]:
            counter = counter + 1
        else:
            output.append(str_list[i].upper())
            output.append(str(counter))
            counter = 1
    return ' '.join(output)

print(run_length_encoding('AAARGGGGGHHHGFFFFF'))