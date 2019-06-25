# n=121
# sum=0
# temp=n
# while(n>0):
#     r=n%10;
#     sum=sum*10+r
#     n=n//10
# if sum==temp:
#     print("Palindrome")
def Palindrome():
    string1= input("enter string")
    flag =True
    for i in range(len(string1)):
        if i!=len(string1)-1-i:
            if string1[i]!= string1[len(string1)-1-i]:
                print("not palindrome")
                break
            else:
                print("palindrome")
                break


Palindrome()    