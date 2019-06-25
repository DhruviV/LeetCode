import heapq
list1=[4,10,3,5,1]
list2=[2,6,8,9,7]
result=[]
heapq.heapify(list1)
print("list1",list1)
heapq.heapify(list2)
print("list2",list2)
while list1 and list2:
    val1 = heapq.heappop(list1)
    val2 = heapq.heappop(list2)
    if val1>=val2:
        heapq.heappush(list1,val1)
        result.append(val2)
    else:
        result.append(val1)
        heapq.heappush(list2,val2)
    heapq.heapify(list1)
    heapq.heapify(list2)
if list1:
    for number in list1:
        result.append(number)
if list2:
    for number in list2:
        result.append(number)
print(result)

