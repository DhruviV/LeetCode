nums=[1,5]
target=2
i=0
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i
    return len(nums)


print(searchInsert(nums,target))

