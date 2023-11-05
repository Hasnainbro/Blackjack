import random
import os
from art import logo

def draw_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computers_score):
    if user_score == computers_score:
        return "It's a Draw😏"
    elif user_score == 0:
        return "You have a Black Jack, You won!🤩"
    elif computers_score == 0:
        return "Oppenent has a Black Jack, You lost😒"
    elif user_score > 21:
        return "You went over, You lost😑"
    elif computers_score > 21:
        return "You win🤩"
    elif user_score > computers_score:
        return "You win🤩"
    else:
        return "You Lose😭"

def play_game():
    print(logo)
    user_cards = []
    computers_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(draw_cards())
        computers_cards.append(draw_cards())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computers_score = calculate_score(computers_cards)
        print(f"User Cards are{user_cards} and User score is {user_score} ")
        print(f"Computer First card is {computers_cards[0]}")


        if user_score == 0 or computers_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to Deal Another Card 'y' for Yes 'n' for No: ")
            if user_should_deal == "y":
                user_cards.append(draw_cards())
            else: 
                is_game_over = True

        while computers_score != 0 and computers_score < 17:
            computers_cards.append(draw_cards())
            computers_score = calculate_score(computers_cards)



    print(f"User Cards are{user_cards} and final score is {user_score} ")
    print(f"Computer cards are {computers_cards} and final score is {computers_score}")

    print(compare(user_score,computers_score))

while input("Do You want to Play the game of Black Jack (type y for yes): ") == "y":
    os.system('cls')
    play_game()
    
