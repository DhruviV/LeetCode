input_list=[1,2,3]
string=""
output_list=[]
for number in input_list:
    temp=str(number)
    string=string+temp

if string.isnumeric():
    print(string)
    output=int(string)+1
    output=str(output)

for char in output:
    output_list.append(int(char))
print(output_list)