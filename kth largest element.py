import heapq
h=[3,2,1,5,6,4]
k=2

heapq.heapify(h)
print(h)
while len(h)!=k:
    print(heapq.heappop(h))

print("kth largest:",h[0])
