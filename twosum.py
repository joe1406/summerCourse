
def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
                


n = [1,2,3,5,6,7,8,9]
print(twoSum(n,17))

