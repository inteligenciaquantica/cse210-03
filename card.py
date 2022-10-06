import random

class Card:
    # this class serves to create car objects
    
    def __init__(self):
        pass
    
    
    def sort_number(self):
        #this method serves to generate a random card between 1 and 13 include them
        self.number = random.randint(1,13)
     
    def return_number(self):
        #this method serves to return the card number
        return self.number
    