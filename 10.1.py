print('Getting a fibonacci sequence')
limit=int(input("Enter the limit of the sequence"))
p=int(0)
q=int(1)
a=[p,q]
z=0
y=0
for x in a:
    b=a[z]
   
    c=a[y]
    
    x=b+c
    if x > limit :
        break
    
    x=str(x)
    a=a.extend(x)
    z+=1
    y+=1
    
print(a)
