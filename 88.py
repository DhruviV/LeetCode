num1=[-1,0,0,3,3,3,0,0,0]
num2=[1,2,2]
i=0
j=0
for i in range(0,len(num1)):
    if num1[i]<=0 and j<len(num2) :
        num1[i]=num2[j]
        j+=1
num1.sort()
print(num1)
