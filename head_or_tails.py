'''
Author: Chris McArthur
Date: 21/08/25
Version: 1.0
Description: This is code for heads or tails 
'''
#-------libraries----------
import random


#-------functions-------------
def heads_tails () :
    user_score=0
    computer_score=0
    options=["Heads", "Tails"]
    while user_score != 2 and computer_score != 2:
        choice=random.randint (0,1)
        computer_guess=options [choice]
        user_guess=str (input ("Heads or Tails") )
  
#-----main----------------
if __name__ == '__main__':
    pass