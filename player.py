
from score import Score

class Player:
    #this class servers to crate player objects
    
    def __init__(self,name,score):
        #this constructor serves to initialize the player's name and score 
        self.name = name
        self.score = score
    
    
    def score(self,score):
        #this method returns the player' score
        return score
        
    def name(self):
        #this method returns the player's name
        return self.name