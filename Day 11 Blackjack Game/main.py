import random

def deal_card():
    """return a random card from the deck"""
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """take a list of cards and calculate the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "draw"
    elif c_score == 0:
        return "Lose, opponent has blackjack"
    elif u_score == 0:
        return "win with a blackjack"
    elif u_score > 21:
        return "You went over, you lose"
    elif c_score > 21:
        return "opponent went over, you win"
    elif u_score > c_score:
        return "You won"
    else:
        return "You lose"

def play_game():
    """play a game of Blackjack"""

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards {user_cards}, current score: {user_score} ")
        print(f"computer cards {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_should_deal = input("Type 'y to get another card, type 'n' to get Pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"your final hands {user_cards}, Final score: {user_score}")
    print(f"computer final hands {computer_cards}, Final score: {computer_score}")
    print(compare(user_score, computer_score))


play_game()