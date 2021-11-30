hours=input('Number of hours worked')
pay=input('pay per hour:')
if hours.isnumeric()==True:
    hours=int(hours)
    reply=""
else:
    reply='Sorry, you entered a string'
print(reply)
if pay.isnumeric()==True:
    pay=int(pay)
    reply1=''
else:
    reply1="sorry you enterd a string"
print(reply1)
total=hours * pay
print(total)
