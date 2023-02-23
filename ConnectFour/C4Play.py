from C4Player import Player
from C4Game import Game

c = Game()
p1 = Player(1, "O")
p2 = Player(2, "X")

while c.win_condition is False:
    
    
    c.turn = p1.end_turn(c.turn)