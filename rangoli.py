n=''
s=''
g=''
num=int(input())
c=''
num1= num+1
b=range(0,num1)
num3=num
for i in range(0,num1):
    i=str(i)
    c+=i
    c+='-'
h=''
k=range(0,num1)
num2=num-1
k=k[num::-1]
for i in k:
    i=str(i)
    h+=i
    h+='-' 
c+=h
z=''
length=len(c)
l=''
i=0
m=''
for i in b:
    n=''
    i=str(i)
    z+=i
    c=len(z)
    c-=1
    x=list(z)
    y=x
    x=x[c::-1]
    g=x.pop()
    for t in x:
      n+=t
      n+='-'
    for t in y:
        n+=t
        n+='-'
    j=''
    j=n.center(length+1,'-')
    print(j)
for i in k:
    m=n
    s=str(i)
    m=m.replace(s,'')
    n=m
    print(m.center(length+3,'-'))
