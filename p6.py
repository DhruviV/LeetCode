list=[1,6,3,9,22,77]
# i want all odds to be on left and even to be on right
def oddeven(list):
    left=0
    right=len(list)-1
    while left<=right:
        if list[left]%2!=0:
            left += 1
        elif list[right]%2==0:
            right -=1
        else:
            temp=list[left]
            list[left]=list[right]
            list[right]=temp
            left+=1
            right-=1
    print(list)




oddeven(list)