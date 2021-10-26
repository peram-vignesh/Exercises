#fint the second highest grade and print the names of the recepients
#alphabaetically using arrays in python
names=[]
marks=[]
final=[]
n=int(input())
while n > 0:
    x=str(input())
    names.append(x)
    y=float(input())
    marks.append(y)
    n-=1
x=max(marks)
y=marks.index(x)
marks.remove(x)
y=names[y]
names.remove(y)
x=max(marks)
z=max(marks)
while x==z:
    y=marks.index(x)
    marks.remove(x)
    b=names[y]
    z=max(marks)
x=max(marks)
while x==z:
    y=marks.index(x)
    marks.remove(x)
    b=names[y]
    names.remove(b)
    final.append(b)
    z=max(marks)
final.sort()
for i in final:
    print(i)
