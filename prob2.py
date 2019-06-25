list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=0
j=1
score=0
n=len(list)
while n>0:
    if list[i]>score:
        print(list[i],"list[i]")
        score=list[i]
        print(list[i])
        for number in list:
            print(number, "number", list[j], "list[j]")

            if number!=list[j]:
                score+=number
                print("score",score)

    i+=1
    n-=1



