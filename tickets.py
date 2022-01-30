print("                 Book My Movie")
print("City's available : Chennai\Hyderabad\Bangalore")
city=(input('Which city do you live in?'))
Chennai=dict()
Hyderabad=dict()
Bangalore=dict()
Chennai['Spiderman']=('IMAX',"Cinepolis",'INOX',"Marina Mall",'SPI Express Mall')
Chennai['83']=("SPI Express Mall","SPI Sathhyam cinemas","PVR cinemas","PVR escape")
Chennai["Pushpa"]=("Gokulam Cinemas","PVR cinemas","Kasi Talkies","Sangam Movies")
Hyderabad['Spiderman']=('Cinepolis Sudha','IMAX',"PVR Cinemas","INOX GVK one")
Hyderabad['83']=('Prasads Multiplex',"Shanthi Theatre",'Suguna Mall')
Hyderabad['Pushpa']=('Shanthi theatres','Alanka Multiplex','Pvr Cinemas')
Bangalore['Spiderman']=('Cinepolis','IMAX',"Inox Garuda Mall","Sangeetha Theatre")
Bangalore['Pushpa']=('Pushpanjali THeatre',"Kapali Theatre",'PVR Bangalore')
Bangalore['83']=('Triveni Theatre','Inox Garuda','PVR Phoenix City','Anupama Theatre')
print('Available movies are : Pushpa\Spiderman\83')
movie=str(input('Movie name:'))
if city=='Chennai':
    x= Chennai[movie]
    for i in x:
        print(i)
elif city=="Bangalore":
    x=Bangalore[movie]
    for i in x:
        print(i)
elif city=="Hyderabad":
    x=hyderabad[movie]
    for i in x:
        print(i)
else:
    print(" City You are searching for isn't available")
y=int(input('Enter the Theatre No.'))
date=str(input('Enter the date of show'))
y-=1
theatre=x[y]
print(" Show Timings For",theatre)
print(''' 1.9:30 a.m. to 12:30 p.m.
2. 1:00p.m. to 4:00p.m.
3. 4:00p.m. to 7:00p.m.,
4. 7:00p.m. to 10:00 p.m.
5. 10:00p.m. to 1:00 a.m.''')
timing=int(input('Enter the show timing(1\2\3\4\5)'))
timing-=1
tickets=int(input('Enter number of tickets'))
cost=tickets* 150
cost+=50
print('It will cost you',cost,'rupees, including gst and internet fees')
time=('.9:30 a.m. to 12:30 p.m.',' 1:00p.m. to 4:00p.m.',' 4:00p.m. to 7:00p.m.',' 7:00p.m. to 10:00 p.m.','5. 10:00p.m. to 1:00 a.m.')
a=time[timing]
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("|        city:",city,'                         Date:',date,'                 |')
print("|        movie:",movie,'           theatre:',theatre,'             |')
print('|        timings:',a,'           cost',cost,'rupees            |')
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
