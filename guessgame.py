x=int(input(''))
y=int(input(''))
import random
n=random.randint (x,y)
player=int(input(''))
while player>0:
    for i in range(1,player+1):
        inp=int(input(''))
        if inp==n:
            print("Player",i,'won the game')
            player=0
            break
        else:
            player=player
    
