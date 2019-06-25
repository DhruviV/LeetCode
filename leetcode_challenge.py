input=[[1,1],[2,3],[3,2]]
x_list=[]
y_list=[]
for n,enumerate in input:
    x_list.append(n)
print("x_list",x_list)
for number in input:
    y_list.append(number[1])
print("y_list",y_list)
x1=x_list[0]
x2=x_list[1]
x3=x_list[2]
y1=y_list[0]
y2=y_list[1]
y3=y_list[2]
print("x1,x2,x3",x1,x2,x3)
print("y1,y2,y3",y1,y2,y3)
b=x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
print(b)
a=0.5*int(b)
print(a)
if a==0:
    print("no")
else:
    print("yes")