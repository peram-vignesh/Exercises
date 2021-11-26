students=int(input())
record={}
s=''
z=''
while students>0:
    a=0
    b=0
    name=input()
    roll=input()
    x=[]
    while 5>a:
        marks=int(input())
        b+=marks
        x.append(marks)
        a+=1
    percentage=b/5
    record[name]=[roll,x,percentage]
    print(record)
    students-=1
print('''Enter 1 for percentage
Enter 2 for maximum marks
Enter 3 to change the name
Enter 4 for entire record''')
y=int(input())
s=input("name")
if y==1:
    for i in record:
        if i == s:
            z=record[s]
            n=z[2]
    print(n)
elif y==2:
    for i in record:
        if i == s:
            z=record[s]
            n=z[1]
    print(max(n))
elif y==3:
    for i in record:
        if i ==s:
            x=input('name')
            x=i
    print(record)
elif y==4:
    for i in record:
        if i== s:
            for i in record[s]:
                print(i)
else:
    print(record)
            
    
   
