#You are given a string S and width .
#Your task is to wrap the string into a paragraph of width W
import textwrap
def wrap (string,width):
    length=len(string)
    y=''
    x=0
    a=width
    while width<length:
        z=string[x:width]
        x+=a
        y+=z
        y+="\n"
        width+=a
    width=width-a
    z=string[width:length]
    y+=z
    return y
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
,
