def count_substring(string, sub_string):
    x=string.find(sub_string)
    
    return x
string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)
