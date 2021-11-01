#In the first line, print True if  has any alphanumeric
#characters. Otherwise, print False.
#In the second line, print True if  has
#any alphabetical characters. Otherwise, print False.
#In the third line, print True if
#has any digits. Otherwise, print False.
#In the fourth line, print True if
#has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if
#has any uppercase characters. Otherwise, print False.
s=input()
s=list(s)
x,y,z,p,q=0,0,0,0,0
for i in s:
    a=i.isalnum()
    b=i.isalpha()
    c=i.isdigit()
    d=i.islower()
    e=i.isupper()
    if a== True:
        x+=1
    if b== True:
        y+=1
    if c== True:
        z+=1
    if d== True:
        p+=1
    if e== True:
        q+=1

def validators(s):
    if s>0:
        t='True'
    else:
        t='False'
    return t
print(validators(x))
print(validators(y))
print(validators(z))
print(validators(p))
print(validators(q))
