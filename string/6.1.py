string=input('Enter the string: ')
count=0
while count<len(string):
    letter=string[count]
    if letter == ":" :
        break
    count=count+1
print (count)
length=len(string)
count=count+1
cut=string[count:length]
if cut.isnumeric()== True :
    cut=float(cut)

else:
    cut='you entered a string after colon'

print (cut)
