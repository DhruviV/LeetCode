def func(num):
    if num==0:
        return [num]

    # # binary = bin(num)
    # print(binary)
    # binary_digits=[]
    count=0
    # while num!=0:
    #     remain=int(num%2)
    #     num=int(num/2)
    #     binary_digits.append(remain)
    # for i in binary_digits:
    #     if binary_digits[i]==1:
    #         count+=1
    # print(count)

    while num > 0:
        # print(num)
        if num & 1 == 1:
            count += 1
        num = num >> 1

    return (count)

    # return list(reversed(binary_digits))
num = int(input("Enter the Number"))
print(func(num))

