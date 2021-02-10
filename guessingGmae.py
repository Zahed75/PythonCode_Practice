import random #generate the random number
guessNumber=int(input("Entter your number:"))
randomNumber=random.randint(1,5) #randiant use for random range 
if guessNumber==randomNumber:
    print("YOU HAVE WON")
else:
     print("YOU HAVE LOSE")
     print("Random number was",randomNumber)