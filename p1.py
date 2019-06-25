def practice():
    string1 = "good"
    string2 = "ogdo"
    dict = {}

    for char1 in string1:
        if char1 in dict:
            dict[char1] += 1
        else:
            dict[char1]=1
    print(dict)

    for char2 in string2:
        if char2 not in dict:
            return "false"
        else:
            dict[char2] -=1
    print(dict)

    for key,value in dict.items():
        if value is 0:
            print("True")
            break

practice()