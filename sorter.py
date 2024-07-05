numbers =  [3,3,4,6,5]

def sorter(list):
	n = 0
	stored_value = list[n] 
	while n < len(list) - 1: 
		if stored_value > list[n+1]: 
			list[n] = list[n+1]
			n = n + 1 
		elif stored_value < list[n+1]: 
			list[n] = stored_value
			stored_value = list[n+1]
			n = n + 1 
		else: #if they are equal
            list[n] = stored_value
            
	list[-1] = stored_value
	

		
numbers =  [4,2,-1,15,6]

def bubble_sort_version_1(items):
    num_items = len(items)
    swap = True
    while swap == True :
        swap = False
        for index in range(0, num_items - 1): 
            if items[index] > items[index + 1]:
                temp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = temp 
                swap = True
        print(items)

bubble_sort_version_1(numbers)