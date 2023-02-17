import random

options = ["r", "p", "s"]
score = { "Player: " : 0, "Computer: " : 0}

def game_logic(player_move, computer_move):
    
    if player_move == computer_move:
        return "You tied!"
    
    elif (player_move == "r" and computer_move == "s") or \
        (player_move == "p" and computer_move == "r") or \
        (player_move == "s" and computer_move == "p"):
        score["Player: "] += 1
        return "You won!"
    
    else:
        score["Computer: "] += 1
        return "You lost!"
    
def game():
    again = "y"
    
    while again == "y":
        player_move = input("Rock (r), paper (p), or scissors (s): ")
        computer_move = random.choice(options)
        print(game_logic(player_move, computer_move))
        
        for n in score:
            print(n, score[n])
        
        again = input("\nPlay again? ('y' for yes): ")

game()