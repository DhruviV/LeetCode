from collections import Counter
input=[10,6,3,6 ]
input.sort()
mydict={}
count=1
for number in input:
    if number not in mydict:
        mydict[number]=count
    else:
        mydict[number]+=1
    count+=1
print(mydict)
ans=[]
for key in mydict:
    if key not in ans:
        ans.append([key,mydict[key]])
print(ans)


