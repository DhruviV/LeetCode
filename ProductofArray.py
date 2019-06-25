nums=[1,2,3,4]
list=[]


for i in range(0,len(nums)):
    iterate = 0
    pointer=i
    mul=1
    print("for loop:",i)
    print("for loop::",pointer)
    while iterate<len(nums):
        print("while:",iterate)
        print("in while:",pointer)
        if iterate==pointer:
            iterate+=1
            print("incremented",iterate)
        else:
            print("multiplying",iterate,nums[iterate])
            mul*=nums[iterate]
            print(mul)
            iterate+=1
            print("incremented",iterate)
    list.append(mul)
print(list)


