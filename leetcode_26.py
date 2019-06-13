nums = [0,0,0,0]
def removeDuplicates(nums):
    if len(nums)==0:
        return len(nums)
    i=0
    for j in range(i+1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]

    return i+1
print(removeDuplicates(nums))