list1=[1,2,3,4,5,5,5,6,7,8,9,1,9]
list1.sort()
print(list1)
print(len(list1))
ans_list=[]
target_value=10
left=0
right=len(list1)-1
while left<=right:
    if list1[left]+list1[right]==target_value:
        ans_list.append([list1[left],list1[right]])
        left+=1
        right-=1
        while left<right and list1[left]==list1[left-1]:
            left+=1
        while left<right and list1[right]==list1[right-1]:
            right-=1
    elif list1[left]+list1[right]<target_value:
        left+=1
    else:
        right-=1
print(ans_list)


