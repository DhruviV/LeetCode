nums=[1,1,0,1,1,1,0]
m=0
c=0
for i in range(0,len(nums)):
    if nums[i]==1:
        c+=1
    else:
        m=max(c,m)
        c=0
m=max(c,m)
print(m)