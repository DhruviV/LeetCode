input=[2,14,18,22,22]
mydic={}
def containsDuplicate(input):
    for number in input:
        if number not in mydic:
            mydic[number]=1
        else:
            mydic[number]+=1
    print(mydic)
    for key in mydic:
        print(mydic[key])
        if mydic[key]>1:
            return True
        else:
            continue
    return False

print(containsDuplicate(input))