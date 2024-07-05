def two_words():
    print('''

This a program that gets two words from the user 
and then displays a message saying if the first word 
can be created using the letters from the second word or not.
          
          ''')
    word1 = input('please enter a first word: ').upper()
    word2 = input('please enter a second word: ').upper()
    list1 = list(word1)
    list2 = list(word2)
    valid = []
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i] == list2[j]:
                valid.append('.')
                list2.pop(j)
                break
    if len(valid) == len(word1):
        print('yes')
    else:
        print('no')

two_words()
