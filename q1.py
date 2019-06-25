string="dhruvi"
list=[]
for char in string:
    list.append(char)

left=0
right=len(string)-1

while left<=right:
    list[left],list[right]=list[right],list[left]
    left+=1
    right-=1
print(list)

