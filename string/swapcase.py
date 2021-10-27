#swap case
def swap_case (word):
    x=""
    word=list(word)
    for i in word:
        if i.isupper()== True:
            i=i.lower()
        else:
            i=i.upper()
            print
        x+=i
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
