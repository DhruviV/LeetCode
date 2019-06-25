version1="0.1"
version2="1.1"
if len(version1)!=1:
    for i in range(1,len(version1)-1):
        if version1[i]!='.':
            print(0)
        else:
            i+=2
if len(version2)!=1:
    for i in range(1,len(version2)-1):
        if version2[i]!='.':
            print(0)
        else:
            i+=2

len1=len(version1)
print(len1)
len2=len(version2)
print(len2)

if len1>len2:
    diff = len1 - len2
    print(diff)
    append = int(diff / 2)
    print(append)
    if append==0:
        append=1
    version2 = version2 + '.0' * append
    print(version2)
else:
    diff=len2-len1
    append=int(diff/2)
    if append==0:
        append=1
    version1=version1+ '.0'*append
    print(version1)

iterate=len(version1)
for i in range(0,iterate-2):
    if version1[i]==version2[i]:
        i+=1
    elif version1[i]>version2[i]:
        print(1)
    else:
        print(-1)

print(0)

