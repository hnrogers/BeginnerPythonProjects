from C4Player import Player
from C4Game import Game

c = Game()
p1 = Player(1, "Heather", "O")
p2 = Player(2, "Bruce", "X")

def play(game, player1, player2):
    while game.win_condition is False:
        if game.turn >= 41:
            print("It's a tie!")
            game.win_condition = True
             
        game.print_game_board()
        game.check = game.get_move(input("Enter column (1-7): "), p1, p2)
        
        if game.check is True:
            if game.turn >= 7:
                game.win_condition = game.check_win(p1, p2)
            game.turn += 1   

play(c, p1, p2)