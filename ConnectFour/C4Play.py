from C4Player import Player
from C4Game import Game

c = Game()
p1 = Player(1, "Heather")
p2 = Player(2, "Bruce")

def play(game, player1, player2):
    while game.win_condition is False:
        game.print_game_board(c)
        game.check = game.check_move(input("Enter column (1-7): "), game.turn)
        
        if game.check is True:
            if game.turn > 8:
                game.win_condition = game.check_win(game.turn, player1, player2)
            game.turn += 1   

play(c, p1, p2)