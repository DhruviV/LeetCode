asteroids=[10,2,-5]
result=[]
for member in asteroids:
    while result and member<0<result[-1]:
        if result[-1]<-member:
            print(result[-1],"result",-member,"member")
            result.pop()
            print("first", result)
            continue

        elif result[-1]==-member:
            print(result[-1], "result", -member, "member")
            result.pop()
            print("second", result)
        break

    else:
        result.append(member)
        print("start",result)

print(result)
