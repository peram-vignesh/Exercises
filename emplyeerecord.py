employees=dict()
employee=int(input())
while employee>0:
    name=input()
    salary=int(input())
    allowance=int(input())
    deduction=int(input())
    gross=salary+allowance
    net=gross-deduction
    employees[name]=[salary,allowance,deduction,gross,net]
    employee-=1
deduct=0
c=0
x=''
y=''
z=''
w=''
a=''
b=''
for i in employees:
    x=employees[i]
    y=x[0]
    z=x[1]
    w=x[2]
    a=x[3]
    b=x[4]
    print('Name:',i,'Salary',y,'allowance:',z,"deduction",w,'gross',a,'net',b)
    c+=z
    deduct+=w
name1=input()
for i in employees:
    if i == name1:
        print(i,'is a employee')
    else:
        print(i,'is not a employee')
