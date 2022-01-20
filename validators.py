s=input()
x,y,z,p,q=0,0,0,0,0
a=s.isalnum()
b=s.isalpha()
c=s.isdigit()
d=s.islower()
e=s.isupper()
print(a,'\n',b,'\n',c,'\n',d,'\n',e)
for i in list (s):
    a=i.isalnum()
    b=i.isalpha()
    c=i.isdigit()
    d=i.islower()
    e=i.isupper()
    if a == True:
        x+=1
    if b == True:
        y+=1
    if c == True:
        z+=1
    if d == True:
        p+=1
    if e == True:
        q+=1
if x>0:
    print('Atleast one character is alphanumeric')
else:
    print('No character is alphanumeric')
if y>0:
    print('Atleast one character is an alphabet')
else:
    print('No character is an alphabet')
if z>0:
    print('Atleast one character is a digit')
else:
    print('No character is a digit')
if p>0:
    print('Atleast one character is of lowercase')
else:
    print('No character is of lowercase')
if q>0 :
    print('Atleast one character is of uppercase')
else:
    print('No character is of uppercase')

