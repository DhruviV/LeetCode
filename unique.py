# def problem():
#     string1="goos"
#     count=0
#     a=len(string1)
#
#
#
#     for i in range(a):
#         for j in range(i+1,a):
#             if string1[i]==string1[j]:
#                 print("yes")

num=int(input("enter number"))
def prime_number(num):
    if num==1:
        return num
    elif num==2 or num%2!=0:
        print("Number is prime")
        return num
    else:
        return num












print(prime_number(num))
# problem()
