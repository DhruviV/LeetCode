A=["amazon","apple","facebook","google","leetcode"]
B=["e","o"]
s=[]
mydict={}

temp=[]
for i in range(0,len(A)):
    for j in range(0,len(A[i])):
        temp.append(A[i][j])

        print(temp)
    count=0
    for character in B:
        if character in temp:
            count+=1
    if count==2:
        print("yes")

