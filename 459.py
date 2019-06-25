from collections import Counter
s="abaababaab"

result=[]
for char in s:
    result.append(char)
print(result)
first=0
check=0
second=1
count=len(result)-1
while count>0:
    if result[first]!=result[second]:
        second+=1
        count-=1
        target=0
    else:
        target=second
        break
print("target",target)
limit=len(result)-target
print("limit",limit)
if target<=0:
    print("No")
elif len(result)%target!=0:
    print("No")
else:
    while limit>0:
        print("i am here")
        if result[target]==result[first]:
            first+=1
            target+=1
            limit-=1
        else:
            print("No")
            break

#         print(first)
#         print(second)
#         new_count=len(result)-1-count
#         while new_count>0:
#             if result[first]!=result[second]:
#                 break
#             else:
#                 first+=1
#                 second+=1
#                 new_count-=1
# print("yes")

