'''
Author: Chris McArthur
Date: 21/08/25
Version: 1.0
Description: This is code for heads or tails 
'''
#-------libraries----------
import random #imports the random library, allowing the use of shuffle, randint, and choice


#-------functions-------------
#-------------------------------------------------------------------------------
#This function gets the user to guess heads or tails until either the player or 
#computer wins, then determines a winner. 
#-------------------------------------------------------------------------------
def heads_tails():
    user_score=0
    computer_score=0
    options=["Heads", "Tails"]
    while user_score != 2 and computer_score != 2:
        choice=random.randint (0,1)
        computer_guess=options [choice]
        user_guess=str(input("Heads or Tails"))
    if user_guess == computer_guess:
        print(f"It was {computer_guess}, you guessed {user_guess}, you won that round")
        user_score +=1
    else:
        print(f"It was {computer_guess}, you guessed {user_guess}, you lost that round")
        computer_score +=1

#-----main----------------
if __name__ == '__main__':
    print("Hi! Welcome to my Heads or Tails game")
    first_name=str(input("What is your name"))
    age=int(input("What is your age"))
    heads_tails() #this calls up the function