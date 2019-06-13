string="abcabcbb"
list=[]
for char in string:
    list.append(char)

check=set(list)
print(len(check))
first=0
count=1
second=first+1
last=len(string)-1
for first in range(last):
    if string[first]==string[second]:
        first+=1
        second+=1
    else:
        count+=1
        second+=1






