import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu= 0
players= 0
y=0
x=''
while y<9:
    players = input("Rock, Paper or  Scissors?").capitalize()
    if players == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu+=1
        else:
            print("You win!", player, "smashes", computer)
            players+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu+=1
        else:
            print("You win!", player, "covers", computer)
            players+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu+=1
        elif computer=="Paper":
            print("You win!", player, "cut", computer)
            players+=1
    if cpu>players:
        y=cpu
        x="CPU"
    elif players>cpu:
        y=players
        x='players'
print(x,'is the winner')
