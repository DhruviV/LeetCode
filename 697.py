from collections import Counter
nums=[1,3,2,2,3,1]

result=[]

def findShortestSubarray(nums):
    list=[]
    count=Counter(nums)
    max=1
    result=[]
    for key in count:
        if count[key]>max:
            max=count[key]

    for key in count:
        if count[key]==max:
            list.append(key)

    for member in list:

        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]==member:
                point_left=left

                break
            else:
                left+=1
        while left<=right:
            if nums[right]==member:
                point_right=right

                break
            else:
                right-=1
        result.append(point_right-point_left+1)

    return min(result)
print(findShortestSubarray(nums))