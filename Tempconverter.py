def converter(value,temp):
    if value =='celcius':
        conver=32/9
        temp=temp/5
        conver+=temp
        conver=int(conver)
        conver=str(conver)
        conver+="'degree Farenheit"
    elif value=="Farenheit":
        conver=32/9
        temp=temp/5
        conver=temp-conver
        conver=int(conver)
        conver=str(conver)
        conver+="'degree celcius"
    return conver
val=str(input())
temp1=int(input())
print(converter(val,temp1))
        
