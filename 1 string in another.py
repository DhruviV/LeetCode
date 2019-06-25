s1="theskyisblue"
s2="the"


mydict={}
for char in s1:
    mydict[char]=1
for char in s2:
    if mydict.get(char)==1:
        val=mydict.get(char)
        mydict[char]=val-1

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
print(fib(3))



