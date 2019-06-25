string="dhruvi"
string2=string[::-1]
print(string2)
list1=[]
for char in string:
    list1.append(char)
print(list1)

left=0
right=len(list1)-1
while left<=right:
    temp=list1[right]

    list1[right]=list1[left]

    list1[left]=temp
    left+=1
    right-=1

print(list1)

