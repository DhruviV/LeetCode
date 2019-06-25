list=[1,0,1]
left=0
right=len(list)
temp=0
for i in range(right):
    if list[i]!=0:
        list[i],list[temp]=list[temp],list[i]
        temp+=1
print(list)
