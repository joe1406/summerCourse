import random

numbers = []

for i in range(21):
    numbers.append(random.randint(0,10))

print(numbers)

def bubblesorter(list):
    for number_of_passes in range(0,len(list)):
        for i in range(0,len(list) - 1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list

print(bubblesorter(numbers))
