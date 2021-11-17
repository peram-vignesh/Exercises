x=str(input())
y=str(input())
dict1=dict()
dict1[x]=0
dict1[y]=0
dict1['others']=0
z=''
while z!='done':
    z=str(input())
    if x == z :
        dict1[x]=dict1[x]+1
    elif y == z :
        dict1[y]=dict1[y]+1
    else:
        dict1['others']=dict1['others']+1
print(dict1)
