s="abb"
left=0
right=len(s)-1
max=0
min=0
while left<=right:
    print("we start here:",left,right,s[left],s[right])
    if s[left]==s[right]:
        print(left)
        print(right)
        print(s[left],s[right])
        max=right
        min=left
        print(max)
        break
    else:
        while left<=right:

        print(right)
        print(s[right])
        right-=1
        if left<=right
print(max)
print(min)

string=''
string=s[min:max+1]
print(string)
palindrome=string[::-1]
if string==palindrome:
    print(palindrome)
