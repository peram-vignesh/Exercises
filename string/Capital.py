#You are asked to ensure that the first and last
#names of people begin with a capital letter in their passports. For example,
#alison heck should be capitalised correctly as Alison Heck.
def solve(s):
    x=''
    s=s.split(' ')
    a=len(s)
    for i in range(0,a):
        a=s[i]
        a=a.capitalize()
        x+=a
        x+=' '
    return x
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
