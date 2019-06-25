# import heapq
# from heapq import nlargest
# list=[10,9,1,2,3]
# max=0
# n=len(list)-1
# for num in list:
#     if num>max:
#         max=num
#
# for num in range(max,0,-1):
#     if num in list:
#         num-=1
#     else:
#         print(num)
#         break
list=[1,2,3]
result=[]
if len(list)>0 or len(list) is 0:
    result.append([])
    result.append(list)

for num in list:
    result.append([num])
print(result)







