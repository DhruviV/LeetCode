s="-S2,_"
new_s=""
list=[]
for character in s:
    list.append(character)
first=0
last=len(list)-1
while first<=last:
    if list[first].isalpha():
        if list[last].isalpha():
            list[last],list[first]=list[first],list[last]
            last -= 1
        else:
            last-=1
    else:
        first+=1

for character in list:
    new_s=new_s+str(character)
print(new_s)


