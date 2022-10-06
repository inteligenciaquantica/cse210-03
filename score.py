


class Score:
    #this class is useful to create score objects
    
    def __init__(self,score):
        #this constructor works to initialize a player's score
        self.score = score
    
    def calculate_score(self,guess,old_card,new_card):
        #this method updates a player' score by using the player's guess, old card, and new card
        #according to the game rules.
        
        print(f"guess: {guess} old_card: {old_card}  new_card: {new_card}")
        if int(old_card) < int(new_card):
            
            if guess=="h": 
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        else:
            if guess=="l": 
                self.score = self.score + 100
            else:
                self.score = self.score - 75
        
    
    def return_score(self):
        #this method returns a player' score updated.
        return self.score