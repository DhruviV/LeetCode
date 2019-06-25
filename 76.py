s="ADOBECODEBANC"
t="ABC"
mydict={}
start,end,i=0,0,0
count=len(t)

for char in t:
    if char not in mydict:
        mydict[char]=1
    else:
        mydict[char]+=1

for j in range(len(s)):
    if s[j] not in mydict:          #"ADOBECODEBANC"
        mydict[s[j]]=0
    else:
        if mydict[s[j]]>0:
            print("mydict",mydict)
            count-=1
            print("co",count)
    mydict[s[j]]-=1

    if count==0:
        print("now count zero")
        while i < j and mydict[s[i]] < 0:
            mydict[s[i]] += 1
            i += 1

            print(mydict,"i am here")

        if  end==0 or j + 1 - i < end - start:
            print("i",i)
            start, end = i, j + 1
            print(start,end)
            print("mydict",mydict)
print(s[start:end])


print(mydict)
print(s[start:end])



        # if not count:
        #     while i < j and char_and_count[s[i]] < 0:
        #         char_and_count[s[i]] += 1
        #         i += 1
        #     if not end or j + 1 - i < end - start:
        #         start, end = i, j + 1

char_and_count, start, end, i, count = {}, 0, 0, 0, len(t)
# for j in range(len(t)):
#     if t[j] not in char_and_count:
#         char_and_count[t[j]] = 1
#     else:
#         char_and_count[t[j]] += 1
#
# for j in range(len(s)):
#
#     if s[j] not in char_and_count:
#         char_and_count[s[j]] = 0
#     else:
#         if char_and_count[s[j]] > 0:
#             count -= 1
#     char_and_count[s[j]] -= 1
# print(char_and_count)