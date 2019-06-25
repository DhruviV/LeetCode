A=[1,2]
B=[3,4]

def MedianArray(A,B):
    len_A = len(A)
    len_B = len(B)
    if len_A>len_B:
        return MedianArray(B,A)
    start, end, combined_mid = 0, len(A), (len_A + len_B + 1) // 2
    while start<=end:
        A_mid=start+end//2
        B_mid=combined_mid-A_mid
    if A_mid<len_A and B[B_mid-1]>A[A_mid]:
        start=A_mid+1
    elif A_mid>0 and A[A_mid-1]>B[B_mid]:
        end=A_mid-1
    else:
        if A_mid==0:
            left_max=B[B_mid-1]
        elif B_mid==0:
            left_max=A[A_mid-1]
        else:
            left_max=max(B[B_mid-1],A[A_mid-1])
        if(len_A+len_B)%2==1:
            return left_max
        if A_mid==len_A:
            right_min=B[B_mid]
        elif B_mid==len_B:
            right_min=A[A_mid]
        else:
            right_min=min(B[B_mid],A[A_mid])
        print((left_max+right_min)/2.0)

print(MedianArray(A,B))