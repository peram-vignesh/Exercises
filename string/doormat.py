a=str(input())
a=a.split(' ')
b=a[0]
c=a[1]
b=int(b)
c=int(c)
x='-'
y='.|.'
e=1
g=b+1
g=g/2
g=int(g)
n=[]
l=0
for i in range (1,b):
    if i%2!=0:
        n.append(i)
n.append(0)
t=n[::-1]
n.remove(0)
for i in t:
    n.append(i)
v=0
while b>=e:
     p=x*c
     d=n[v]
     q=y*d
     if e==g:
        print('WELCOME'.center(c,x))
     else:
        print(q.center(c,x))
     e+=1
     v+=1
