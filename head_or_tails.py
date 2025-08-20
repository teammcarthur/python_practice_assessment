'''
Author: Chris McArthur
Date: 21/08/25
Version: 1.0
Description: This is code for heads or tails 
'''
#-------libraries----------
import random


#-------functions-------------
#This function gets the user to guess heads or tails until either the player or 
#computer wins, then 

def heads_tails () :
    user_score=0
    computer_score=0
    options=["Heads", "Tails"]
    while user_score != 2 and computer_score != 2:
        choice=random.randint (0,1)
        computer_guess=options [choice]
        user_guess=str (input ("Heads or Tails") )
    if user_guess == computer_guess:
        print ("It was {}, you guessed {}, you won that round".format (computer_guess, user_guess) )
        user_score +=1
    else:
        print ("It was {}, you guessed {}, you lost that round".format (computer_guess, user_guess) )
        computer_score +=1

#-----main----------------
if __name__ == '__main__':
    pass