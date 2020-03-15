from random import shuffle
from time import sleep


last_saldo = 0
card_list = list()


def main():

    make_deck()
    shuffle(card_list)

    if last_saldo == 0:
        print("This is a BlackJack game!\n")

        while True:
            try:
                know_rules = input("Do You know the rules?: ")
                if know_rules.lower()[0] == "y":
                    know_rules = True
                    break
                elif know_rules.lower()[0] == "n":
                    know_rules = False
                    break
                else:
                    print('Say "yes" or "no"')
            except:
                print('Say "yes" or "no"')


        if not know_rules:
            print("The rules:")
            print("Computer starts with one veiled card and you hit once.\nThen you and computern"
                  " can hit (take random card from deck) or stand.\nYou have to be closer than computer to 21 points.")
            print("When game starts you can bet with your money (100$).\nIf You win your doubled bet is going back to You.")
            input("\nPress Enter to start!")


    while True:
        try:
            player_bet = int(input("What is Your bet?: "))
            if player_bet >= 0 and player_bet <= 100:
                break
            else:
                print('Wrong value! You have 100$ on start.')
        except:
            print('Wrong value!')

    print(" ")
    sleep(1)
    dealer = Dealer()
    print(" ")
    sleep(1)
    player = Player(player_bet)
    print(" ")
    sleep(1)
    dealer.hit()
    while True:

        if not player.is_standing:
            while True:
                try:
                    print(" ")
                    hit_or_stand = input("Would you rather hit or stand?: ")
                    if hit_or_stand.lower()[0] == "h":
                        player.hit()
                        break
                    elif hit_or_stand.lower()[0] == "s":
                        player.stand()
                        break
                    else:
                        print('Say "hit" or "stand"')
                except:
                    print('Say "hit" or "stand"')
        else:
            player.stand()

        sleep(1)
        print(" ")
        dealer.decide()
        sleep(1)
        if  dealer.is_standing and player.is_standing:
            print(" ")
            if game_ends(player.points,dealer.points) == "Player wins!":
                player.win()
                print("Player wins!")
            elif game_ends(player.points,dealer.points) == "Draw!":
                player.draw()
                print("Draw!")
            else:
                print(print("Dealer wins!"))

            print(f"Player: {player.points} --- Dealer: {dealer.points}")
            break



    print("Your balance is now " + str(player.saldo) + "$!")


    return player.saldo




def make_deck():
    card_list.clear()
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



def game_ends(p_points,d_points):

    difference_player = abs(21 - p_points)
    difference_dealer = abs(21 - d_points)
    if difference_player > difference_dealer:
        return("Dealer wins!")
    elif difference_player ==  difference_dealer:
        return("Draw!")
    else:
        return ("Player wins!")






class Player():

    def __init__(self,player_bet):
        self.saldo = 100
        self.player_bet = player_bet
        self.bet()
        self.points = 0
        self.hit()
        self.is_standing = False


    def stand(self):
        self.is_standing = True
        print("You are standing")


    def hit(self):
        new_card = card_list.pop()

        if new_card.value == "to set":
            new_card.check_if_ace_method(True)

        print("Your hit is "+str(new_card))

        self.points += new_card.value
        print(f"You have {self.points} points now!")

        del(new_card)


    def bet(self):
        self.saldo -= self.player_bet


    def win(self):
        self.saldo += 2*self.player_bet


    def draw(self):
        self.saldo += self.player_bet




class Dealer():

    def __init__(self):
        self.points = 0
        self.first_hit = True
        self.hit()
        self.is_standing = False



    def decide(self):
        if self.points >= 17:
            self.stand()
        else:
            self.hit()


    def stand(self):
        self.is_standing = True
        print("Dealer is standing")



    def hit(self):
        new_card = card_list.pop()

        if new_card.value == "to set":
            new_card.check_if_ace_method(False,self.points)

        if self.first_hit:
            print("Dealer takes first card!")
            self.first_hit = False
        else:
            print("Dealer hits for "+str(new_card))

        self.points += new_card.value
        del (new_card)



class Card():

    def __init__(self,suit,type,value):
        self.suit = suit
        self.type = type
        self.value = value
        self.name_suit_method()
        self.refresh_name_method()



    def check_if_ace_method(self,if_player,d_points=0):
        if self.value == "to set":
            one_or_eleven = None
            if if_player:
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

            else:
                if d_points > 10:
                    self.value = 11
                else:
                    self.value = 1

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



    def __del__(self):
        pass




if __name__ == "__main__":
    while True:
        last_saldo = main()
        while True:
            try:
                again = input("Do You want to play again?: ")
                if again.lower()[0] == "y":
                    again = True
                    break
                elif again.lower()[0] == "n":
                    again = False
                    break
                else:
                    print('Say "yes" or "no"')
            except:
                print('Say "yes" or "no"')
        if not again:
            break