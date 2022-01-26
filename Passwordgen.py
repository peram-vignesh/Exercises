def password(limit,name,length):
    import random
    list1='1234567890;,./`~!@+=!@#$%^&*:<>?|\''
    list1=list(list1)
    num=random.randint(0,length)
    part1=name[0:num]
    x=len(part1)
    while limit > x:
        rand=random.choice(list1)
        part1+=rand
        x=len(part1)
    return part1
name1=str(input('Enter your name:'))
limit1=int(input('Enter the limit of password'))
if limit1 < 8:
    limit1=8
length1=len(name1)
if length1>limit1:
    y=length1-limit1
    y+=4
    length1-=y

print("Your password suggestion 1",password(limit1,name1,length1))
print("Your password suggestion 2",password(limit1,name1,length1))
print("Your password suggestion 3",password(limit1,name1,length1))
