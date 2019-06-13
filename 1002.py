from collections import Counter
list=["cool","lock","cook"]
new_list=[]

result = []
if not list :
    print(result)
c = Counter(list[0])

for s in list :
    c &= Counter(s)
    mydict=c
for key in mydict:
    new_list.append(str(key))
print(new_list)