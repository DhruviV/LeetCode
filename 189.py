
nums=[1,2,3,4,5,6,7]
k=3
left=0
right=len(nums)-1
for i in range(k):
    nums.insert(0,nums.pop())
print(nums)

# while k>0:
#     print("left",nums[left])
#     print("right",nums[right])




