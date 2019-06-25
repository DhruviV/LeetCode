from itertools import permutations
l=list(permutations(range(0,3)))
print(l)
string="abcd"
permlist=permutations(string)
for i in list(permlist):
    print(''.join(i))
