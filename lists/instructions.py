#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.

a=list()
n=int(input())
x=''
while n > 0:
    add=str(input())
    add=add.split(' ')
    x=add[0]
    add.remove(x)
    try:
        c=int(add[0])
    except:
        add=add
    if x== 'append':
        a.append(c)
    elif x=='insert':
        b=int(add[1])
        a.insert(c,b) 
    elif x=='remove':
        a.remove(c) 
    elif x=="reverse":
        b=len(a)
        a=a[b::-1]  
    elif x=='sort':
        a.sort()
    elif x== 'print':
        print(a)
    elif x=='pop':
        b=len(a)
        b= b-1
        b=a[b]
        a.remove(b)
    n-=1
