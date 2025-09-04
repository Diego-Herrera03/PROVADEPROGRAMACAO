def translate_card_to_number(brute_card):
    card = brute_card.lower()

    try:
        if card == "a" or card == "1":
            return "1"
        
        elif card == "2":
            return "2"
        
        elif card == "3":
            return "3"
        
        elif card == "4":
            return "4"
        
        elif card == "5":
            return "5"
        
        elif card == "6":
            return "6"
        
        elif card == "7":
            return "7"
        
        elif card == "8":
            return "8"
        
        elif card == "9":
            return "9"
        
        elif card == "10":
            return "10"
        
        elif card == "j":
            return "11"
        
        elif card == "q":
            return "12"
        
        elif card == "k":
            return "13"
        
        else:
            return

    except Exception as e:
        print(e)


def translate_card_suit_to_number(suit):
    try:
        if suit == "clubs" or suit == "c":
            return "1"

        elif suit == "hearts" or suit == "h":
            return "2"

        elif suit == "spades" or suit == "s":
            return "3"

        elif suit == "diamonds" or suit == "d":
            return "4"

        else:
            return 
        
    except Exception as e:
        print(e)


def translate_card_weight_to_number(brute_card):
    try:
        card = translate_card_to_number(brute_card)

        low_cards  = ["4", "5", "6", "7"]
        mid_cards  = ["11", "12"]
        high_cards = ["13", "1", "2", "3"]

        if card in low_cards:
            return 1

        elif card in mid_cards:
            return 0

        elif card in high_cards:
            return -1

        else:
            return
    
    except Exception as e:
        print(e)


def translate_card_suit_weight_to_number(brute_suit):
    try:
        suit = translate_card_suit_to_number(brute_suit)

        mid_suit = ["2", "3"]

        if suit == "1":
            return -1

        elif suit in mid_suit:
            return 0

        elif suit == "4":
            return 1
        
    except Exception as e:
        print(e)


sum_card = 0
sum_card_suit = 0


while True:
    card = input("Type your card :\n>>>")
    suit = input("Type your card suit: \n>>>")

    card_number             = translate_card_to_number(card)
    card_suit_number        = translate_card_suit_to_number(suit)
    card_number_weight      = translate_card_weight_to_number(card)
    card_suit_number_weight = translate_card_suit_weight_to_number(suit)

    sum_card += card_number_weight
    sum_card_suit += card_suit_number_weight

    print(f"\n\n\nSum of the cards weight: {sum_card}\nSum of the cards suits weight:{sum_card_suit}\n\n\n")
