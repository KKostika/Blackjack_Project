import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card = []
c_card = []
c_total = sum(c_card, 0)
total = sum(card, 0)


def blackjack():
    card3 = int()
    c_card3 = int()
    print(logo)
    card1, card2 = random.sample(cards, 2)
    card.append(card1)
    card.append(card2)
    print(f"Your cards:{card}, current score: {card1 + card2}")
    c_card1, c_card2 = random.sample(cards, 2)
    c_card.append(c_card1)
    c_card.append(c_card2)
    c_total = c_card1 + c_card2 + c_card3
    print(f"Computers first card: {c_card1}")
    more = input("Type 'y' to get another card, type 'n' to pass:\n")
    if more == 'y':
        extra = random.choice(cards)
        card.append(extra)
        card3 += extra
        total = card1 + card2 + card3
        print(f"    Your cards: {card}, current score: {total}")
        print(f"    Computer's first card: {c_card1}")
        more = input("Type 'y' to get another card, type 'n' to pass:")

    else:
        total = card1 + card2 + card3
        while c_total < 17 and c_total < total:
            pc_extra = random.choice(cards)
            c_card.append(pc_extra)
            c_card3 += pc_extra

            compare()


def final_hand():
    c_total = sum(c_card, 0)
    total = sum(card, 0)
    print(f"    Your final hand: {card}, final score: {total}")
    print(f"    Computer's final hand: {c_card}, final score: {c_total}")


def compare():

    if total > 21:
        final_hand()
        print("You went over. And now you are a LOSER \N{loudly crying face}!!!")
    elif c_total > 21 and total <= 21:
        final_hand()
        print("You ve won. Computer went over!")
    elif total <= 21 and total > c_total:
        final_hand()
        print("You've won \N{smiling face with sunglasses}!!!")
    elif total <= 21 and total < c_total:
        final_hand()
        print("You lose\N{unamused face}")
    else:
        final_hand()
        print("It is a draw darling, another one?\N{slightly smiling face}")


def start():
    begin = input("Do you want to play a game of BlackJack? Type 'y' or 'n':\n")

    if begin == 'y':
        print("\n * 20")
        blackjack()
        compare()
        start()

    else:
        print("GoodBye")


start()
