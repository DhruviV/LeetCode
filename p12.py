list1=[1,7,5,9,2,12,3]
k=2
dict={}


def cal(list1,k):
    answer_list = []
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]-list1[j]==2 or list1[i]-list1[j]==-2:
                answer_list.append([list1[i],list1[j]])
    return answer_list

print(cal(list1,k))