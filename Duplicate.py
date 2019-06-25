list=[1,3,4,2,2]
first=0
second=first+1
dict={}
for number in list:
    if number in dict:
        val=dict.get(number)
        dict[number]=val+1
        print(number)
    else:
        dict[number]=1

print(dict)
