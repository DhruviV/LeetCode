A=[3,1,2,4]
left=0
right=len(A)-1
while left<=right:
    print(A[left])
    if A[left]%2==0:
        print(A[left])
        print("i am even here")
        left+=1
    else:
        print("i am here")
        if A[right]%2==0:
            print("i am odd here")
            A[left],A[right]=A[right],A[left]
            print(A[left],A[right])
            print(A)
            right-=1
        else:
            right-=1

print(A)