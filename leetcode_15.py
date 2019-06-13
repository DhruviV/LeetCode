nums=[-2,0,1,1,2]
nums.sort()
result=[]
def threeSum(nums):
    i=0
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        k=len(nums)-1
        j=i+1
        ans=-nums[i]
        while j < k:
            if nums[j]+nums[k]==ans:
                result.append([nums[i],nums[j],nums[k]])
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
            elif nums[j]+nums[k]<ans:
                j+=1
            else:
                k-=1
    return result


print(threeSum(nums))






