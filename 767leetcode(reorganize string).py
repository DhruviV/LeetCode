import collections
s="aabbc"
list=[]
for char in s:
    list.append(char)
print(list)
print(collections.Counter(list))

for i in range(0,len(list)-1):
    j=i+1
    if list[i]==list[j]:
        j+=1
        if list[i]==list[j]:
            j+=1
        else:
            list[j],list[j-1]=list[j-1],list[j]
            j+=1
            i+=1
    else:
        i+=1
        j+=1
print(list)
for i in range(0,len(list)-1):
    if list[i]==list[i+1]:
        print("")
    else:
        output_s="".join(list)
    i+=1
print(output_s)





















