import collections
s=""
t=""

if s is None and t is None:
    print("true")


mydict=collections.Counter(s)


for char in t:
    if char not in mydict:
        print("false")
        break
print("true")



