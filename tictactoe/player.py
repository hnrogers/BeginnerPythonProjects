import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
    
    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

###

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly choose one
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, game_state, player):
        max_player = self.letter    # yourself!
        other_player = 'O' if player == 'X' else 'X'
        
        # check if previous move is a winner
        # with recursion you always need a base case
        if game_state.current_winner == other_player:
            return {'position': None, 'score': 1 * (game_state.num_empty_squares() + 1) if other_player == max_player else -1 * (game_state.num_empty_squares + 1) }
        
        elif not game_state.empty_squares():    #no empty squares
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf} # each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf} # each score should minimize
        
        for possible_move in game_state.available_moves():
            # step 1: make a move, try that spot
            game_state.make_move(possible_move, player)
        
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(game_state, other_player) # now we alternate players
            
            # step 3: undo the move so we can try the next one in a future iteration
            game_state.board[possible_move] = ' '
            game_state.current_winner = None
            sim_score['position'] = possible_move   # otherwise this will get messed up from recursion
            
            # step 4: pdate the dictionaries if necessary (if score in current move beats current best score)
            if player == max_player:    #trying to maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score  # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best
        return best