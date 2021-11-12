#fibanacci sequence
numbers=int(input('Enter the range of the sequence'))
x=0
a=0
b=0
y=[0,1]
print(x)
while a<= numbers:
    x=int(y[a])
    b=int(y[a+1])
    z=x+b
    y.append(z)
    print(z)
    a+=1
print(y)
