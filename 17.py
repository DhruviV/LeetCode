digits=23
phone={2:['a','b','c'],
       3:['d','e','f'], 4:['g','h','i'],
       5:['j','k','l'],6:['m','n','o'],
       7:['p','q','r','s'],8:['t','u','v'],
       9:['w','x','y','z']}
temp2=digits%10
temp1=int(digits/10)
digits=[]
digits.append(temp1)
digits.append(temp2)
list1=[]

ans=[""]
for digit in digits:
       list1=phone[digit]
       list2=[]
       for mem in list1:
              for members in ans:
                     list2.append(members+mem)
       ans=list2
print(ans)






