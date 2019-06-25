list1=["flower","flight","flow"]
shortest_str = min(list1,key=len)

def prefix(list1):
    for i,char in enumerate(shortest_str):
        for other in list1:
            if other[i]!=char:
                return(shortest_str[:i])

print(prefix(list1))

