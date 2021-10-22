#palindrome
string=str(input('enter'))
length=len(string)
x=string
y=string[length-1::-1]
if x==y:
    print(string,'is a palindrome')
else:
    print(string,'is not a palindrome')

