'''
You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...

To play a hand of Blackjack the following steps must be followed:

Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again

Playing Cards
A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks
(2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks,
Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting.
'''


card_list = list()


class Card():

    def __init__(self,suit,type,value):
        self.suit = suit
        self.type = type
        self.value = value
        self.name_suit_method()
        self.refresh_name_method()
        #self.check_if_ace_method()



    def check_if_ace_method(self):
        if self.value == "to set":
            one_or_eleven = None
            while True:
                try:
                    one_or_eleven = int(input('Would you like "Ace" to be 1 or 11?: '))
                    if one_or_eleven == 1 or one_or_eleven == 11:
                        self.value = one_or_eleven
                        break
                    else:
                        print("That's not " + '"1"' + " or " + '"11"')
                except:
                    print("That's not " + '"1"' + " or " + '"11"')
            self.refresh_name_method()

        else:
            pass


    def name_suit_method(self):

        if self.suit == 1: self.suit = "Club"
        if self.suit == 2: self.suit = "Spade"
        if self.suit == 3: self.suit = "Diamond"
        if self.suit == 4: self.suit = "Heart"



    def full_card_name_method(self):
        if self.type == "Rank":
            self.full_name = f'"{self.value} of {self.suit}s" with value {self.value}'
        else:
            self.full_name = f'"{self.type} of {self.suit}s" with value {self.value}'



    def __str__(self):
        return(self.full_name)



    def refresh_name_method(self):
        self.full_card_name_method()
        self.__str__()






def main():
    make_deck()

    for card in card_list:
        print(str(card))
    print(len(card_list))







def make_deck():
    for i in range(2,15):
        for j in range(1,5):
            if i == 14:
                card_list.append(Card(suit=j, type="Ace", value="to set"))
            elif i == 11:
                card_list.append(Card(suit=j, type="Jack", value=10))
            elif i == 12:
                card_list.append(Card(suit=j, type="Queen", value=10))
            elif i == 13:
                card_list.append(Card(suit=j, type="King", value=10))
            else:
                card_list.append(Card(suit=j, type="Rank", value=i))





if __name__ == "__main__":
    main()