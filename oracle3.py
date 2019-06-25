arr=[10, 5, 3, 4, 3, 5, 6]
mydict={}
for number in arr:
    if number in mydict:
        val=mydict[number]
        mydict[number]+=1
    else:
        mydict[number]=1
print(mydict)
for key in mydict:
    if mydict[key]>1:
        print(key)
        break



