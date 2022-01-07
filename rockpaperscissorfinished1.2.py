import random
def rock_paper_scissor_determine_victor(user_action, computer_action):  
    if user_action == computer_action:
      print(f'both players selected {user_action}')  
      return(0,0)
       
    elif(user_action == "rock" and computer_action == "paper" 
     or (user_action == "paper" and computer_action == "scissor")
     or (user_action == "scissor" and computer_action == "rock")):
       print(f"computer wins!{computer_action} beats {user_action}")
       return (0,1)
    else:
      print(f"you win!{user_action} beats {computer_action}")
    return(1,0)
    
def rock_paper_scissor_best_of_five():
     total_user_victory = 0
     total_computer_victory = 0
     while total_user_victory < 3 and total_computer_victory < 3:
       user_action = input("Enter a choice (rock, paper, scissor): ")
       possible_action = ["rock", "paper", "scissor"]
       computer_action = random.choice(possible_action)
     print(f"\n You chose{user_action}, computer chose {computer_action}.\n")
     (user_victory, computer_victory)= rock_paper_scissor_determine_victor(user_action, computer_action)
     total_user_victory += user_victory
     total_computer_victory += computer_victory
     rock_paper_scissor_best_of_five()
