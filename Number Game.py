import random
playing=True
number=str(random.randint(0,10000))

print(" I will think of a number between 0 and 10,You only get 1 chance only to guess the number right! ")
while playing:
  guess=input("What is your guess? ")  
  if number==guess:
   print("Congratulations! You guessed the number right!")
   print("The number was "+number)
   break
  
  else:
   print("Wrong guess! Try again!")
   print("The number was "+number+" Lol u guessed from 1 to 10 ") 
after=input("Do you want to play again? (yes/no) ")
if after=="yes":
  playing=True
else:  playing=False
 