x=str(input("Enter the name of the key"))
y=str(input("enter the name the key"))
dict1=dict()
dict1[x]=0
dict1[y]=0
dict1['others']=0
z=''
while z!='done':
    z=str(input('Enter the strings'))
    if x == z :
        dict1[x]=dict1[x]+1
    elif y == z :
        dict1[y]=dict1[y]+1
    else:
        dict1['others']=dict1['others']+1

print(dict1)
