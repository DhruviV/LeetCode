nums=[[1,[1,3]],[2,[4,5]],[5,[6,7]]]
my_calendar=[{"id":1,"day":"Monday"},{"id":2,"day":"Tuesday"},{"id":3,"day":"Monday"},
             {"id":4,"day":"Tuesday"}]
mydict={}
list=[]
for number in nums:
    print(number[1][1])


for member in my_calendar:
    if member["day"] in mydict:
        mydict[member["day"]]+=1
    else:
        mydict[member["day"]]=1

print(mydict)
input=100
ans={"peny":0,"dine":0,"quarter":0}
def cashregister(money):
    if money<10:
        temp=money/1
        ans["peny"]=temp
        return ans

    elif money>=10 and money<25:
        if money%10==0:
            temp=int(money/10)
            ans["dine"]=temp
            return ans
        else:
            temp=money%10
            diff=int(money/10)
            ans["dine"]=diff
            ans["peny"]=temp
            return ans


    else:
        if money%25==0:
            temp=int(money/25)
            ans["quarter"]=temp
            return ans
        else:
            temp=int(money/25)
            ans["quarter"]=temp
            diff=int(money%25)
            if diff<10:
                ans["peny"]=diff
            else:
                temp=int(diff/10)
                ans["dine"]=temp
                temp2=int(diff%10)
                ans["peny"]=temp2

            return ans
print(cashregister(input))
number=123
print(bin(number))