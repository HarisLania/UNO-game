#importing necessary libraries
import random
import sys

#Cards in deck = 58
#red-green-yellow-blue
#(0-9),drawtwo,skip,reverse-1s(each colour)
#wild-4
#draw-four-2

colors = ['red','green','yellow','blue']
special = ['draw_four','wild']
numbers = ['zero','one','two','Three','four','five','six','seven','eight','nine','draw-2','skip','reverse']
values = {'Zero':['red','green','yellow','blue'],
'One':['red','green','yellow','blue'],
'Two':['red','green','yellow','blue'],
'Three':['red','green','yellow','blue'],
'Four':['red','green','yellow','blue'],
'Five':['red','green','yellow','blue'],
'Six':['red','green','yellow','blue'],
'Seven':['red','green','yellow','blue'],
'Eight':['red','green','yellow','blue'],
'Nine':['red','green','yellow','blue'],
'draw-2':['red','green','yellow','blue'],
'skip':['red','green','yellow','blue'],
'reverse':['red','green','yellow','blue']
}


class Cards:
    def __init__(self,number,color):
        self.number = number
        self.color = color

    def __str__(self):
        return "{} in {}".format(self.number,self.color)

#Cards are distibuted in them and rest are in deck_list which is the attribute of class Deck
player = dict()
comp = list()

class Deck(Cards):
    def __init__(self):
        self.deck_list = []

    def deck_making(self):
        for color in colors:
            for number in numbers:
                self.deck_list.append(Cards(number, color))
                #if number != numbers[0]:
                #    self.deck_list.append(Cards(number,color))

        for i in range(2):
            for card in special:
                if card == 'wild':
                    self.deck_list.append(card)
                self.deck_list.append(card)

    #only if you want to check the cards in deck and its length
    def getCards(self):
        for card in self.deck_list:
            print(card)
        print(len(self.deck_list))

    def distribute_cards(self):
        random.shuffle(self.deck_list)
        #print('{:>40}{:>40}'.format('Player','Computer'))
        for i in range(1,9):
            player[i]= str(self.deck_list.pop())
            comp.append(str(self.deck_list.pop()))
        print('Cards have been distributed.....')
        #print('Your cards: ', player)
        print('Your cards, ')
        print(player)
        #for i,j in player.items():
         #   print(i,j)
#        for j in range(8):
#            print('{:>40} {:>40}'.format(player[j],comp[j]))



deck = Deck()
deck.deck_making()
#print(len(deck.deck_list))
#after distributing then get cards
deck.distribute_cards()

#------------------------------------Area for playing

class PlayingArea(Deck):
    def __init__(self,card='',turn='player',status=None):
        self.card = card
        self.turn = turn
        self.status = status

    #card are assigned from here
    def mainCard(self,card):
        print('{:>80}'.format('|     -------------------------------    |'))
        print('{:>80}'.format('|     -------------------------------    |'))
        #print('------------------------------------------------------------------------------------------------------------------------------------')
        if self.card[:7] == 'reverse':
            print('{:>65}'.format('{}           ').format(card))
        elif self.card == 'wild' or self.card == 'draw_four':
            print('{:>70}'.format('{}           ').format(card))
        else:
            print('{:>67}'.format('{}           ').format(card))
        print('{:>80}'.format('|     -------------------------------    |'))
        print('{:>80}'.format('|     -------------------------------    |'))
        #print('-------------------------------------------------------------------------------------------------------------------------------------')
        #print('--------------------------------------------------------------------------------------------------------------------------------------')


    #the first card came from here
    def area(self):
        random.shuffle(deck.deck_list)
        self.card = str(deck.deck_list.pop())
        if self.card[:4] == 'draw' or self.card[:4] == 'wild' or self.card[:4] == 'skip'  or self.card[:7] == 'reverse':
            deck.deck_list.append(self.card)
            self.area()
        else:
            self.mainCard(self.card)


    #its for the turn
    def ask(self):
        #print('Deck: ',len(deck.deck_list))
        if self.turn == 'player':
            print('---Your turn---')
            for i, j in player.items():
                print(i, j)
            self.turn = 'comp'
            self.player_game()
        else:
            print(comp)
            print('{:>110}'.format('--Computer turn--'))
            self.turn = 'player'
            self.comp_game()

    #the player bank
    def get_bankcard(self):
        stuff = []
        for i in player.keys():
            stuff.append(i)
        a = str(deck.deck_list.pop())
        deck.deck_list.append(a)
        random.shuffle(deck.deck_list)
        player[stuff[-1] + 1] = a
        print('From bank..', stuff[-1] + 1, player[stuff[-1] + 1])

    def wild(self):
        red = 0
        blue = 0
        green = 0
        yellow = 0
        greatest = ''
        for i in comp:
            if 'red' in i:
                red += 1
            elif 'blue' in i:
                blue += 1
            elif 'green' in i:
                green += 1
            elif 'yellow' in i:
                yellow += 1

        #print(red)
        #print(blue)
        #print(green)
        #print(yellow)

        if (red >= blue) and (red >= yellow) and (red >= green):
            greatest = 'red'
        elif (blue >= red) and (blue >= yellow) and (blue >= green):
            greatest = 'blue'
        elif (green >= blue) and (green >= yellow) and (green >= red):
            greatest = 'green'
        elif (yellow >= blue) and (yellow >= red) and (yellow >= green):
            greatest = 'yellow'

        #print(greatest)

        if self.card == 'wild':
            self.card = 'Wild: ' + greatest
        else:
            self.card = 'Draw four: ' + greatest


    #bank for computer
    def comp_bank(self):
        a = str(deck.deck_list.pop())
        comp.append(a)
        deck.deck_list.append(a)
        random.shuffle(deck.deck_list)

    #for draw_four
    def ask_color(self):
        col = input('Enter color: ').lower()
        if col in colors:
            if self.card == 'wild':
                self.card = 'Wild: ' + col
            else:
                self.card = 'Draw four: ' + col
        else:
            self.ask_color()

    def player_last_card(self):
        print('--------UNO----------')
        print('Last card cannot be that ')
        print('Adding two cards..')
        self.get_bankcard()
        self.get_bankcard()
        self.player_game()

    def comp_last_card(self):
        print('--------UNO----------')
        print('Last card cannot be that ')
        print('Adding two cards..')
        self.comp_bank()
        self.comp_bank()
        self.comp_game()


    #all the functionalities of player
    def player_game(self):
        if len(player) == 1 and ('wild' in player.values() or 'draw_four' in player.values()):
            self.player_last_card()
        else:
            if len(player) > 0:
                bank_ask = input('Want to get card from bank?(y/n)').lower()
                if bank_ask == 'y':
                    self.get_bankcard()
                    ask = input('Do you get the required card now:(y/n)').lower()
                    if ask == 'y':
                        try:
                            card_name = int(input('Enter card id(1,2....):'))
                            if card_name in player.keys():
                                if player[card_name][-3:] == self.card[-3:] or player[card_name][-4:] == self.card[-4:] or player[card_name][-5:] == self.card[-5:] \
                                        or player[card_name] == 'wild' or player[card_name] == 'draw_four' \
                                        or player[card_name][:3] == self.card[:3] or player[card_name][:5] == self.card[:5] or player[card_name][:4] == self.card[:4] \
                                        or player[card_name][:6] == self.card[:6] or player[card_name][:7] == self.card[:7]:
                                    self.card = player[card_name]
                                    if self.card[:5] == 'draw-':
                                        del player[card_name]
                                        self.comp_bank()
                                        self.comp_bank()
                                        self.mainCard(self.card)
                                        print('{:>110}'.format('Two cards given to computer'))
                                        self.ask()
                                    elif self.card[:4] == 'skip' or self.card[:7] == 'reverse':
                                        del player[card_name]
                                        self.mainCard(self.card)
                                        print('Still your turn..')
                                        for i, j in player.items():
                                            print(i, j)
                                        self.player_game()
                                    elif self.card == 'wild':
                                        self.ask_color()
                                        del player[card_name]
                                        self.mainCard(self.card)
                                        self.ask()
                                    elif self.card == 'draw_four':
                                        del player[card_name]
                                        self.comp_bank()
                                        self.comp_bank()
                                        self.comp_bank()
                                        self.comp_bank()
                                        self.ask_color()
                                        print('{:>110}'.format('Four cards given to computer'))
                                        self.ask()
                                    else:
                                        del player[card_name]
                                        self.mainCard(self.card)
                                        self.ask()


                                elif player[card_name] != self.card:
                                    print('No cheating.....')
                                    self.player_game()

                        except ValueError:
                            print('Invalid syntax..')
                            self.player_game()

                        else:
                            print('No cheating.....')
                            self.player_game()

                    elif ask == 'n':
                        self.ask()

                    else:
                        self.ask()

                elif bank_ask == 'n':
                    try:
                        card_name = int(input('Enter card id(1,2....):'))
                        if card_name in player.keys():
                            if player[card_name][-3:] == self.card[-3:] or player[card_name][-4:] == self.card[-4:] or player[card_name][-5:] == self.card[-5:] \
                                    or player[card_name] == 'wild' or player[card_name] == 'draw_four' \
                                    or player[card_name][:3] == self.card[:3] or player[card_name][:5] == self.card[:5] or player[card_name][:4] == self.card[:4] \
                                    or player[card_name][:6] == self.card[:6] or player[card_name][:7] == self.card[:7]:
                                self.card = player[card_name]
                                if self.card[:5] == 'draw-':
                                    del player[card_name]
                                    self.comp_bank()
                                    self.comp_bank()
                                    self.mainCard(self.card)
                                    print('{:>110}'.format('Two cards given to computer'))
                                    self.ask()
                                elif self.card[:4] == 'skip' or self.card[:7] == 'reverse':
                                    del player[card_name]
                                    self.mainCard(self.card)
                                    print('Still your turn..')
                                    for i, j in player.items():
                                        print(i, j)
                                    self.player_game()
                                elif self.card== 'wild':
                                    self.ask_color()
                                    del player[card_name]
                                    self.mainCard(self.card)
                                    self.ask()
                                elif self.card == 'draw_four':
                                    del player[card_name]
                                    self.comp_bank()
                                    self.comp_bank()
                                    self.comp_bank()
                                    self.comp_bank()
                                    self.ask_color()
                                    self.mainCard(self.card)
                                    print('{:>110}'.format('Four cards given to computer'))
                                    self.ask()
                                else:
                                    del player[card_name]
                                    self.mainCard(self.card)
                                    self.ask()

                            elif player[card_name] != self.card:
                                print('No cheating.....')
                                self.player_game()

                    except ValueError:
                        print('Invalid syntax..')
                        self.player_game()

                    else:
                        print('No cheating.....')
                        self.player_game()

                else:
                    self.player_game()
                self.ask()

            else:
                self.mainCard(self.card)
                print('{:>60}'.format('Congratulation you won....'))
                sys.exit(0)




    def chk_comp(self):
        for i in range(len(comp)):
            if self.card[-3:] == comp[i][-3] or self.card[-4:] == comp[i][-4:] or self.card[-5:] == comp[i][-5:] or comp[i] == 'wild' or comp[i] == 'draw_four' \
                    or self.card[:3] == comp[i][:3] or self.card[:4] == comp[i][:4] or self.card[:5] == comp[i][:5] or self.card[:6] == comp[i][:6] \
                    or self.card[:7] == comp[i][:7]:
                self.status = True
                break
            else:
                self.status = False

    def comp_game(self):
        if len(comp) == 1 and ('wild' in comp or 'draw_four' in comp):
            self.comp_last_card()
        else:
            while len(comp) > 0:
                self.chk_comp()
                if self.status == True:
                    print('{:>110}{}'.format('The computer remaining cards: ',len(comp) - 1 ))
                    for card in comp:
                        if self.card[-3:] == card[-3:] or self.card[-4:] == card[-4:] or self.card[-5:] == card[-5:] or card == 'wild' or card == 'draw_four' \
                                or self.card[:3] == card[:3] or self.card[:4] == card[:4] or self.card[:5] == card[:5] or self.card[:6] == card[:6] \
                                or self.card[:7] == card[:7]:
                            self.card = card
                            if self.card[:5] == 'draw-':
                                comp.remove(self.card)
                                self.mainCard(self.card)
                                print('Two cards given to you')
                                self.get_bankcard()
                                self.get_bankcard()
                                self.ask()
                            elif self.card[:4] == 'skip' or self.card[:7] == 'reverse':
                                comp.remove(self.card)
                                self.mainCard(self.card)
                                self.comp_game()
                            elif self.card == 'wild':
                                comp.remove(self.card)
                                self.wild()
                                self.mainCard(self.card)
                                self.ask()
                            elif self.card == 'draw_four':
                                comp.remove(self.card)
                                self.wild()
                                self.mainCard(self.card)
                                print('Four cards given to you')
                                for i in range(4):
                                    self.get_bankcard()
                                self.ask()
                            else:
                                self.mainCard(self.card)
                                comp.remove(self.card)
                                self.ask()

                elif self.status == False:
                    self.comp_bank()
                    print('{:>110}'.format('Computer picked a card from bank'))
                    print('{:>110}{}'.format('The computer remaining cards: ',len(comp)))
                    for card in comp:
                        if card[-3:] == self.card[-3:] or card[-4:] == self.card[-4:] or card[-5:] == self.card[-5:] or card == 'wild' or card == 'draw_four' \
                            or self.card[:3] == card[:3] or self.card[:4] == card[:4] or self.card[:5] == card[:5] or self.card[:6] == card[:6] \
                            or self.card[:7] == card[:7]:
                            self.card = card
                            if self.card[:5] == 'draw-':
                                comp.remove(self.card)
                                self.mainCard(self.card)
                                print('Two cards given to you')
                                self.get_bankcard()
                                self.get_bankcard()
                                self.ask()
                            elif self.card[:4] == 'skip' or self.card[:7] == 'reverse':
                                comp.remove(self.card)
                                self.mainCard(self.card)
                                self.comp_game()
                            elif self.card == 'wild':
                                comp.remove(self.card)
                                self.wild()
                                self.mainCard(self.card)
                                self.ask()
                            elif self.card == 'draw_four':
                                comp.remove(self.card)
                                self.wild()
                                self.mainCard(self.card)
                                print('Four cards given to you')
                                for i in range(4):
                                    self.get_bankcard()
                                self.ask()

                            self.mainCard(self.card)
                            comp.remove(self.card)
                            self.ask()

                        else:
                            print('{:>110}'.format('Still nothing'))
                            self.mainCard(self.card)
                            self.ask()

                    self.ask()
            else:
                self.mainCard(self.card)
                print('{:>65}'.format('You Lost...'))
                sys.exit(0)


ground = PlayingArea()
ground.area()
ground.ask()
#ground.create_stuff()

