


# def binary_search_iterative(list,target):
#     found = False
#     lower_bound = 0 
#     upper_bound = len(list) - 1 
#     pivot = (lower_bound + upper_bound + 1)//2 
#     while not found and lower_bound <= upper_bound:
#         if target > list[pivot]: 
#             lower_bound = pivot + 1
#         elif target < list [pivot]:
#             upper_bound = pivot - 1 
#         else:
#             found = True
#             return 'found at index ', pivot
#         pivot = (lower_bound + upper_bound + 1)//2 
#     return 'not present'

# print(binary_search_iterative(numbers,8))
numbers = [2,4,6,7,8,10]
def binary_search_recursive(list,target):
    lower_bound = 0 
    upper_bound = len(list) - 1 
    pivot = (lower_bound + upper_bound + 1)//2 
    if lower_bound >= upper_bound:
        return 'not present'
    if target == list[pivot]:
        return 'found'
    else:
        if target < list[pivot]:
            return binary_search_recursive(list[lower_bound:pivot],target)
        elif target > list[pivot]:
            return binary_search_recursive(list[pivot:upper_bound+1],target)


print(binary_search_recursive(numbers,2))






    


    

        


