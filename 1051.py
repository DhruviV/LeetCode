heights=[1,1,4,2,1,3]
correct_order=[]
count=0
for number in heights:
    correct_order.append(number)
correct_order.sort()
print(correct_order)
print(heights)
for i in range(0, len(heights)):
    if heights[i]!=correct_order[i]:
        count+=1
    i+=1
print(count)




