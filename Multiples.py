x=int(input())
y=int(input())
z=int(input())
a=int(input())
for i in range(x,y):
    if i%z==0:
        print(i,'is a multiple of',z)
        l=0
    else:
        l=1
    if i%a==0:
        print(i,'is a multiple of',a)
        n=0
    else:
        n=2
    if l==n:
        print(i,'is a multiple of',z*a)
    
