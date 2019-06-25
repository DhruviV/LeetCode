def isValid(s):
    mydict = {")": "(", "}": "{", "]": "["}
    stack=[]
    for char in s:
        print("string mem",char)
        if char in mydict:
            print("char",char)
            if stack:
                top=stack.pop()
            else:
                top="*"
            if top!=mydict[char]:
                return False
        else:
            stack.append(char)
            print(stack,"stack")
    return not stack
print(isValid("()[]"))