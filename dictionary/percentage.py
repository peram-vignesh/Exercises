#finding percentage
marks=dict()
students=int(input())
name=''
y=''
z=()
a=0.00
while students>0:
    score=str(input())
    index=score.split(" ")
    for i in index:
        try:
            i=float(i)
            i=i
        except:
            y=i
    index.remove(y)
    marks[y]=index
    students-=1
name=str(input())
z=marks[name]
for i in z:
    try:
        i=float(i)
        a= a+i
    except:
        i=str(i)
a=a/3.00  
print(("{0:.2f}".format(a)))
