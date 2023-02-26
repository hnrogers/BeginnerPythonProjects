import re
from C4Player import Player
import math

class Game:
    def __init__(self): # initiates game board [7 x 6 list of lists]
        self.game_board = [["_" for i in range(7)] for a in range(6)]
        self.turn = 1
        self.check = False
        self.win_condition = False
        self.letter_count = 0
        self.y = 0  # y = which list
        self.x = 0  # x = list position
    
    def print_game_board(self): # works
        for x in self.game_board:
            print(*x, sep=" | ")
    
    def try_parse(self, column): # converts input to number or default (to pick again)
        try:
            column = int(column)
            return column
        except ValueError:
            return 9
    
    def get_move(self, x, player1, player2):    # checks for empty spaces in selected x, returns T/F  
        self.x = self.try_parse(x) - 1
        player = player1 if self.turn % 2 != 0 else player2  # get current player
        
        if self.x > 7 or self.x < 0:
            print("Invalid selection! \n")
            return False
        
        for i in reversed(range(0,6)):
            if self.game_board[i][self.x] == "_":
                self.game_board[i][self.x] = player.p_letter
                self.y = i
                print()
                print(self.y, self.x, sep=", ")
                return True
            
        print("Column full! \n")
        return False

    def check_win(self, player1, player2):
        
        player = player1 if self.turn % 2 != 0 else player2  # get current player
        self.letter_count = 1
        end_check = False
                       
        while self.letter_count < 4 and end_check is False:
            
            self.letter_count = self.horizontal(player)
            
            if self.letter_count >= 4:
                continue
            else:
                self.letter_count = 1
                self.letter_count = self.vertical(player)
            
            if self.letter_count >= 4:
                continue
            else:
                self.letter_count = 1            
                self.letter_count = self.diagonal1(player)
                
            if self.letter_count >= 4:
                continue
            else:
                self.letter_count = 1
                self.letter_count = self.diagonal2(player)
            
            end_check = True
            
        if self.letter_count >= 4:
            self.print_game_board()
            print(f"{player.p_name} wins :)")
            return True
        
        if self.turn >= 41:
            self.print_game_board()
            print("It's a draw!")
            return True
        
        return False 
    
    def horizontal(self, player):   # works :)
        to_edge_max = 6 - self.x
        self.letter_count = 1
        
        while self.letter_count < 4:
            for i in range(1, (to_edge_max + 1)):
                if self.game_board[self.y][self.x + i] == player.p_letter:
                    self.letter_count += 1
                
                elif self.letter_count == 4:
                    return self.letter_count
                
                elif self.game_board[self.y][self.x + 1] == "_":
                    break
            
            if self.x == 0:
                return 0
              
            for i in range(1, (self.x + 1)):
                if self.game_board[self.y][self.x - i] == player.p_letter:
                    self.letter_count += 1
                elif self.letter_count >= 4:
                    return self.letter_count
                else:
                    return 0
            return self.letter_count if self.letter_count >= 4 else 0
    
    def vertical(self, player): # works :)
        to_edge_min = 5 - self.y
        self.letter_count = 1
        
        while self.letter_count < 4:
            for i in range(1, (to_edge_min + 1)):
                if self.game_board[self.y + i][self.x] == player.p_letter:
                    self.letter_count += 1
                else:
                    break
                
            return self.letter_count if self.letter_count >= 4 else 1
    
    def diagonal1(self, player):
        
        if (6 - self.x) > (self.y):     # check distance to go (pos)
            to_edge_max = self.y
        else:
            to_edge_max = 6 - self.x                
         
        for i in range(1, (to_edge_max + 1)):
            if self.game_board[self.y - i][self.x + i] == player.p_letter:
                self.letter_count += 1
            elif self.game_board[self.y - i][self.x + i] == "_":
                break
        
        if self.x == 0 or self.y == 5 or self.letter_count >= 4:  # check distance to go (neg) or quit
            return self.letter_count
        elif (self.x) > (5 - self.y):
            to_edge_min = 5 - self.y
        else:
            to_edge_min = self.x
        
        for i in range(1, (to_edge_min + 1)):
            if self.game_board[self.y + i][self.x - i] == player.p_letter:
                self.letter_count += 1
            elif self.game_board[self.y + i][self.x - i] == "_":
                break
        
        return self.letter_count if self.letter_count >= 4 else 1
    
    def diagonal2(self, player):
            
        if (self.x) > (self.y):     # check distance to go (up)
            to_edge_max = self.y
        else:
            to_edge_max = self.x                
         
        for i in range(1, (to_edge_max + 1)):
            if self.game_board[self.y - i][self.x - i] == player.p_letter:
                self.letter_count += 1
            elif self.game_board[self.y - i][self.x - i] == "_":
                break
        
        if self.x == 6 or self.y == 5 or self.letter_count >= 4:  # check distance to go (neg) or quit
            return self.letter_count
        elif (6 - self.x) > (5 - self.y):
            to_edge_min = 5 - self.y
        else:
            to_edge_min = 6 - self.x
        
        for i in range(1, (to_edge_min + 1)):
            if self.game_board[self.y + i][self.x + i] == player.p_letter:
                self.letter_count += 1
            elif self.game_board[self.y + i][self.x + i] == "_":
                break
        
        return self.letter_count if self.letter_count >= 4 else 1