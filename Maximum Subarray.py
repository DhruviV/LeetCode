import heapq
nums=[8,-19,5,-4,20]

result=[]
heapq.heapify(nums)
dict={}
for number in nums:
    if number in dict:
        val=dict.get(number)
        dict[number]=val+1
    else:
        dict[number]=1

for key in dict:
    result.append(key)
print(result)
max =1
while len(result)-1:
    new=sum(result)
    heapq.heappop(result)
    check=sum(result)
    if check>new:
        new=check
print(new)




