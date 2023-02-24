import re
from C4Player import Player
import math

class Game:
    def __init__(self): # initiates game board [7 x 6 list of lists]
        self.game_board = [["_" for i in range(7)] for a in range(6)]
        self.turn = 1
        self.check = False
        self.win_condition = False
        self.y = 0
        self.x = 0
    
    def print_game_board(self, game): # works
        for x in self.game_board:
            print(*x, sep=" | ")
    
    def try_parse(self, column): # converts input to number or default (to pick again)
        try:
            column = int(column)
            return column
        except ValueError:
            return 9
    
    def get_move(self, x, turn, player1, player2):    # checks for empty spaces in selected x, returns T/F  
        self.x = self.try_parse(x) - 1
        player = player1 if turn % 2 != 0 else player2  # get current player
        
        if self.x > 7 or self.x < 0:
            print("Invalid selection! \n")
            return False
        
        for i in reversed(range(6)):
            if self.game_board[i][self.x] == "_":
                self.game_board[i][self.x] = player.p_letter
                self.y = i
                print()
                return True
            
        print("Select another x! \n")
        return False

    def check_win(self, turn, player1, player2, row, column):
        
        player = player1 if turn % 2 != 0 else player2  # get current player
                    
        letter_count = 1
        to_edge_max = 0
        to_edge_min = 0
        next = False
        
        # row win first
        to_edge_max = 6 - column  # forward n spaces till edge
        to_edge_min = column
        
        while letter_count < 4 and next is False:
            for i in range(1, (to_edge_max + 1)):
                if self.game_board[row][column + i] == player.p_letter:
                    letter_count += 1
                elif letter_count == 4:
                    break
                
            for i in range(1, (to_edge_min + 1)):
                if self.game_board[row][column - i] == player.p_letter:
                    letter_count += 1
                elif letter_count == 4:
                    break
                else:
                    letter_count = 1
                    break
            next = True
        
        # column win
        #to_edge_max = 5 - row
        #to_edge_min = row
        #next = False
        
        #while letter_count < 4 and next is False:
        #    pass
            
        if letter_count == 4:
            self.print_game_board(self.game_board)
            print(f"{player.p_name} wins :)")
            return True
        
        return False 