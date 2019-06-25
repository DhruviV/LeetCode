num=int(input("enter number"))
def func(num):
    count=0
    if num == 0:
        return num
    while  num > 0:
        if num & 1 == 1:
            count +=1
        num = num >> 1
    print(count)
    return num


func(num)
