num=38

def ans(num):
    if num>=10:
        temp1=num%10
        temp2=int(num/10)
        new=temp1+temp2
        return ans(new)

    else:
        
        return num
print(ans(num))