string="a good    example"
store=string.split()
print(store)
left=0
right=len(store)-1
while left<=right:
    store[left],store[right]=store[right],store[left]
    left+=1
    right-=1

print(" ".join(store))
