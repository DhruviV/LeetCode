strs=["eat","tea","tan","ate","nat","bat"]
dict={}
list=[]
for i in strs:
    x="".join(sorted(i))
    print(x)

    if x in dict:
        dict[x].append(i)

    else:
        dict[x]=[i]
print(dict)
for key in dict:
    list.append(dict[key])
print(list)


