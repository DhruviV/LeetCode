string="aba"
n=121
temp=n
sum=0
r=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if temp==sum:
    print("true")
else:
    print("false")
first=0
last=len(string)-1
while first<=last:
    if string[first]==string[last]:
        first+=1
        last-=1

    else:
        print("Not a palindrome")
        break
Given a string of words with numbers and special characters interspersed throughout, remove the special characters and numbers.
 Then print the remaining words in sorted order one word per line.  