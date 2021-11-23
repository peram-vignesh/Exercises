entries=int(input('entries'))
list1=dict()
while entries>0:
    country=input('country')
    capital=input('Capital')
    currency=input('currency')
    list1[country]=(capital,currency)
    entries-=1
print('Country \t\t capital \t currency\t\t')
x=''
y=''
z=''
for i in list1:
    x=list1[i]
    y=x[0]
    z=x[1]
    print(i,'\t\t',y,'\t\t',z)
select=input()
for i in list1:
    x=list1[i]
    y=x[0]
    z=x[1]
    if i==select:
        print(i,'\t',y,'\t',z)
    
    
    
