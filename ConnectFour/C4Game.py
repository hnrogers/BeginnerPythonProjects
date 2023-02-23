import re
from C4Player import Player
import math

class Game:
    def __init__(self): # initiates game board [7 x 6 list of lists]
        self.game_board = [["_" for i in range(7)] for a in range(6)]
        self.turn = 1
        self.win_condition = False
    
    def print_game_board(self): # works
        for row in self.game_board:
            print(*row, sep=" | ")
    
    def try_parse(self, r): # converts input to number or default (to pick again)
        try:
            r = int(r)
            return r
        except ValueError:
            return 9
    
    def check_move(self, r, turn):    # checks for empty spaces in selected row, returns T/F  
        r = self.try_parse(r) - 1
        
        if r > 7 or r < 0:
            print("Invalid selection! \n")
            return turn
        
        for i in reversed(range(6)):
            if self.game_board[i][r] == "_":
                if turn % 2 != 0:
                    self.game_board[i][r] = "O"
                else:
                    self.game_board[i][r] = "X"
                print()
                return turn
            
        print("Select another row! \n")
        return turn

    def check_win(self, turn):
        for row in self.game_board:
            if re.search("(OOOO)", ''.join(row)) or re.search("(XXXX)", ''.join(row)):
               print("Player 1 wins!" if turn % 2 != 0 else "Player 2 wins!")
               return True
        
        return False 

t = Game()
t.print_game_board()
win_condition = False

while win_condition is False:
    t.check_move(input("Enter row (1-7): "), t.turn)
    t.print_game_board()
    win_condition = t.check_win(t.turn)
    t.turn += 1