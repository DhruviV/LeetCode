nums=[1,2,1,2,4,5]
k=0

if k<0:
    print("0")
if k==0:
    dict={}
    for i in nums:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    count=0
    for i in dict.values():
        if i>1:
            count+=1
    print(count)
num2=[i+k for i in nums]
print(len(set(num2))& len(set(nums)))