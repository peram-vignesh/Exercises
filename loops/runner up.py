#finding runner up score
def runner(score):
   winner= max(score)
   score.remove(winner)
   runner=max(score)
   while runner==winner:
       score.remove(runner)
       runner=max(score)
   
   return runner          
students=int(input())
marks=list(input())
print(runner(marks))
