def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            sum = nums[i] + nums[i+j+1]
            if sum == target:
                return [nums[i],nums[i+j+1]]
            
print(twoSum([3,3],6))