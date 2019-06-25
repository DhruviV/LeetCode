from itertools import combinations
n=4
k=2
list=[]
for i in range(1,n+1):
    list.append(i)
print(list)
combo=combinations(list,k)
for i in combo:
    print(i)




