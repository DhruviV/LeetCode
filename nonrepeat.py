string="abbac"
def nonrepeat(string):
    for i in range(0,len(string)):
        if string[i] != string[i+1]:
            print(string[i+1])
            break

nonrepeat(string)
