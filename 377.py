from itertools import permutations
nums=[1,2,3]

res=[]
ans=[]
target=4
dp=[0]*(target+1)
print(dp)
dp[0]=1
print("now",dp  )
nums.sort()
for i in range(1,target+1):
    for n in nums:
        print("i am i",i,"i am num",n)
        if n>i:
            break
        print(dp[i],"dp[i]")
        print(dp[i-n],"dp[i-n]")
        dp[i]+=dp[i-n]
        print(dp)
print(dp[-1])













