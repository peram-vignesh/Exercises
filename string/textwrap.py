#cutting text according to input,n
string=str(input('string'))
width =int(input('width'))
x=len(string)
while x > width:
    x=len(string)
    if x>=width:
        i=string[0:width]
        string=string[width:x]
    else:
       i=string
    print(i)
    print(string)
    x=x-width
    
   
