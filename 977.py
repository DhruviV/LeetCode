input=[-4,-1,0,3,10]
input.sort()
result=[]
for number in input:
    number=number*number
    result.append(number)
result.sort()
print(result)
