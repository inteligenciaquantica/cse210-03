from player import Player
from score import Score
from card import Card

def main():
    print("\n")
    print("************************   Hilo Game *************************")
    player_number = int(input("Type de number of players: "))
    player_list = []
    score = 300    
    for i in range(player_number):
        name = input(f"Type the name's player ({i+1}): ")
        pl = Player(name,score)
        player_list.append(pl)
    answer = 'y'
    
    
    play(player_list,player_number,score)
    
    


def play(player_list,player_number,score):
    #this function run the game by using the player list, plyer number, and initial player' score
    for j in range(player_number):
        print(f"Player: {player_list[j].name}   Score: {player_list[j].score}")
    answer = 'y'
    card = Card()
    sc = Score(score)
    while(answer=='y'):
        
        card.sort_number()
        old_card = card.return_number()
        print(f"The card is: {old_card}")
        guess = input(f"Higher or lower (h/l)? ")
        card.sort_number()
        new_card = card.return_number()
        print(f"Next card was: {new_card}")
        
        sc.calculate_score(guess,old_card,new_card)
        print(f"Your score is: {sc.return_score()}")
        answer = input("Play again? [n/y] ")

if __name__=="__main__":
    main()