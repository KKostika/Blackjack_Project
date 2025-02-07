import random
from art import logo


def final_hand():
    print(f"    Your final hand: {card}, final score: {total}")
    print(f"    Computer's final hand: {computers_card}, final score: {computers_total}")


def compare():
    if total > 21:
        final_hand()
        print("You went over. And now you are a LOSER \N{loudly crying face}!!!")
    elif computers_total > 21 and total <= 21:
        final_hand()
        print("You ve won. Computer went over!")
    elif total <= 21 and total > computers_total:
        final_hand()
        print("You've won \N{smiling face with sunglasses}!!!")
    elif total <= 21 and total < computers_total:
        final_hand()
        print("You lose\N{unamused face}")
    else:
        final_hand()
        print("It is a draw darling, another one?\N{slightly smiling face}")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card = []
computers_card = []
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
if start == 'y':
    print(logo)
    card1, card2 = random.sample(cards, 2)
    card.append(card1)
    card.append(card2)
    computers_card1, computers_card2 = random.sample(cards, 2)
    computers_card.append(computers_card1)
    computers_card.append(computers_card2)

    print(f"    Your cards: {card}, current score: {card1 + card2}")
    print(f"    Computer's first card: {computers_card1}")
    more = input("Type 'y' to get another card, type 'n' to pass:")
    card3 = int()
    computers_card3 = int()
    computers_total = computers_card1 + computers_card2 + computers_card3
    total = card1 + card2 + card3

    if more == 'y':
        extra = random.choice(cards)
        card.append(extra)
        card3 += extra
        total = card1 + card2 + card3
        print(f"    Your cards: {card}, current score: {total}")
        print(f"    Computer's first card: {computers_card1}")
        more = input("Type 'y' to get another card, type 'n' to pass:")

    else:
        is_game_over = True

    while computers_total < 19 and computers_total < total:
        pc_extra = random.choice(cards)
        computers_card.append(pc_extra)
        computers_card3 += pc_extra
        computers_total = computers_card1 + computers_card2 + computers_card3

    compare()

else:
    print("GoodBye!")

