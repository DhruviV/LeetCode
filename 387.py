s="cc"
mydict = {}
list = []
s1 = []
if s == "":
    print("-1")
for char in s:
    if char in mydict:
        mydict[char] += 1
    else:
        mydict[char] = 1
for key in mydict:
    if mydict[key] == 1:
        list.append(key)
print(mydict)

if not list:
    print("-1")
else:
    for char in s:
        s1.append(char)
        i = 0
    for i in range(0, len(s1)):
        if s1[i] in list:
            print(i)



n=[["a","b"],["c","d"]]
for a,enumerate in n:
    print(a)



