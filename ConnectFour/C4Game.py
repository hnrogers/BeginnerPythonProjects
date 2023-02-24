import re
from C4Player import Player
import math

class Game:
    def __init__(self): # initiates game board [7 x 6 list of lists]
        self.game_board = [["_" for i in range(7)] for a in range(6)]
        self.turn = 1
        self.check = False
        self.win_condition = False
    
    def print_game_board(self, game): # works
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
            return False
        
        for i in reversed(range(6)):
            if self.game_board[i][r] == "_":
                if turn % 2 != 0:
                    self.game_board[i][r] = "O"
                else:
                    self.game_board[i][r] = "X"
                print()
                return True
            
        print("Select another row! \n")
        return False

    def check_win(self, turn, player1, player2):
        for row in self.game_board: # horizonal check
            if re.search("(OOOO)", ''.join(row)) or re.search("(XXXX)", ''.join(row)):
               print(f"{player1.p_name} wins!" if turn % 2 != 0 else f"{player2.p_name} wins!")
               return True
        
        return False 