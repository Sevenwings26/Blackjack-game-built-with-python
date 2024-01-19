############### Blackjack Project #####################

import random
from clear import clear_screen
from blackjack_logo import logo

# function performing random card selection 
def deal_cards():
    """ Returns a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

# function to compare user_score and computer_score 
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponect has balckjack " 
    elif user_score == 0:
        return "WIn with a Blackjack " 
    elif user_score > 21:
        return "You went over, You lose " 
    elif computer_score > 21:
        return "Opponent went over, You Win "
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    # Store cards here
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Execute random twice
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # function to calculate cards in list 
    def calculate_score(cards):
        """Takes a list of cards and return the score calculated from the cards."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        
        """Check if Ace = 11 or 1"""
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}.")
        print(f" Computer's first card: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True
                
    """Computer keeps drawing if less than 17"""
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score =calculate_score(computer_cards)

    print(f" Your final hand: {user_score}, final score: {user_score}")
    print(f" Computer's final hand: {computer_score}, final score: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    clear_screen()
    print(logo)
    play_game()
    
    
