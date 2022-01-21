def computegrade(marks) :
    grades='EDCBA'
    list1=[char for char in grades]
    grade=list1[marks]
    return grade
marks=int(input('Enter the marks: '))
if marks<5:
    marks=5
marks-=5
print(computegrade(marks))
