import math
totalcrates=6
allLocations=[[3,6],[2,4],[5,3],[2,7],[1,8],[7,9]]
trunkCapacity=3
result=[]
allLocations.sort()
if not allLocations:
    print([])
dist=[]
dictionary={}
for a in allLocations:
    temp=math.sqrt((0-a[0])*(0-a[0])+(0-a[1])*(0-a[1]))
    dictionary[temp]=a

for key in dictionary:
    dist.append(key)
dist.sort()
for i in range(trunkCapacity):
     result.append(dictionary[dist[i]])
print(result)





