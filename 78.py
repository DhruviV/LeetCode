from itertools import combinations
nums=[1,2,3]
final_num=list(set(nums))
def subs(final_num):
    res = []
    for i in range(1, len(final_num) + 1):
        print(i)
        for combo in combinations(final_num, i):
            res.append(list(combo))
    return res
print(subs(final_num))