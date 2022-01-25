candidate=int(input("Number of candidates"))
votes={}
while candidate>0:
    name = str(input("Enter the name of the candidate"))
    votes[name]=0
    candidate-=1
voters=int(input("Number of voters"))
while voters>0:
    try:
        vote=str(input('Who are you voting to?'))
        votes[vote]+=1
        surity=str(input('Confirm your vote'))
        if surity=='yes':
            votes=votes
        else:
            votes[vote]-=1
            print('Please start your voting process from begining')
            voters+=1
    except:
        print('The entered member is not on the list')
        print('Please start your voting process from begining')
        voters+=1
    voters-=1
winner=sorted(votes.items(),key=lambda votes: votes[1])
x=winner.pop()
y=x[0]
print(y,'is the winner')
