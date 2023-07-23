import random

def play():
    user = input("'r' for rock, 'p' for paper, 's for scissors'" )
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It is a tie"
    
    if is_win(user, computer):
        return "You Win!"
    
    return "You lost"

#defining the player winning function
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r' ):
        return True
    

