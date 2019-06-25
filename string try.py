from itertools import permutations
import sys

string1="abcd"
check= None
# k=4
# permlist=permutations(string1,k)
# for i in list(permlist):
#     print(i)
for i in range(1,len(string1)-1):
    str2=string1[:i]
    print(str2)
    check=True

print(sys.maxsize)
print(check)
print(-sys.maxsize-1)