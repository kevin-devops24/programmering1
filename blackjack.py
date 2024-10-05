import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.value.isnumeric():
                value += int(card.value)
            else:
                if card.value == "Ace":
                    aces += 1
                    value += 14
                else:
                    value += 10

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def __repr__(self):
        return f"Hand value: {self.calculate_value()} with cards: {self.cards}"


# Create a deck and shuffle it
deck = Deck()
deck.shuffle()

# Create player and dealer hands
player_hand = Hand()
dealer_hand = Hand()

# Deal initial cards
player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())

dealer_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())

# Display initial hands
print("You have been dealt two cards:")
print(player_hand)
print("The dealer has one card face up and one card face down.")

# Player's turn
while True:
    action = input("Do you want to 'hit' or 'stand'? ")
    if action.lower() == "hit":
        player_hand.add_card(deck.deal())
        print("You have been dealt another card:")
        print(player_hand)
        if player_hand.calculate_value() > 21:
            print("You busted! The dealer wins.")
            break
    elif action.lower() == "stand":
        break
    else:
        print("Invalid input. Please enter 'hit' or 'stand'.")

# Dealer's turn
while dealer_hand.calculate_value() < 17:
    dealer_hand.add_card(deck.deal())

print("The dealers face-down card is:")
print(dealer_hand.cards[1])
print("The dealers face-up card is:")
print(dealer_hand.cards[0])
print("The dealer has finished playing cards.")

# Determine winner
if dealer_hand.calculate_value() > 21:
    print("The dealer busted! You win!")
elif dealer_hand.calculate_value() < player_hand.calculate_value():
    print("Your hand value is higher than the dealers. You win!")
elif dealer_hand.calculate_value() > player_hand.calculate_value():
    print("The dealers hand value is higher than yours. You lose.")
else:
    print("It's a tie!")