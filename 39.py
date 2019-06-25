from itertools import combinations
candidates=[10,1,2,7,6,1,5]
target=8
result=[]
# result=[seq for i in range(len(candidates),0,-1) for seq in combinations(candidates,i) if sum(seq)==target]
# print(result)
for i in range(0,len(candidates)):
    combo=combinations(candidates,i)

    for i in combo:
        if sum(i)==target:
            print(i)
            result.append(i)
print(result)

# import itertools
# numbers = [1, 2, 3, 7, 7, 9, 10]
# result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 10]
# print(result)
