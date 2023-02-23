class Player:
    def __init__(self, p_num, p_symbol):
        self.p_number = p_num # 1 or 2
        self.p_symbol = p_symbol
    
    def end_turn(self, t):
        self.t = t + 1
        return self.t