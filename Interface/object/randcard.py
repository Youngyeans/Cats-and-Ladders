import pygame
import random

class Card(object):
    def __init__(self):
        self.chanelcard = {
            'ch10' : [1,10],
            'ch15' : [2,5],
            'ch20' : [2,10],
            'ch29' : [3,9],
            'ch37' : [4,7],
            'ch52' : [6,2],
            'ch56' : [6,6],
            'ch61' : [7,1],
            'ch71' : [8,1],
            'ch77' : [8,7],
            'ch86' : [9,6],
            'ch93' : [10,3],
            'ch98' : [10,8]
        }

        self.row_card = 1
        self.column_card = 1
        self.rolling_card = False

        self.randomcard = 0
        self.player_stop = 5

        self.card_images = []
        self.card_spin_images = []
        self.card_spin_count = 0
        self.spining = False
        for i in range(1,7):
            self.card_image = pygame.transform.scale(pygame.image.load('Art/Card_' + str(i) + '.png'), (298.5,495))
            self.card_images.append(self.card_image)

        for i in range(1,19):
            self.card_spin_image = pygame.transform.scale(pygame.image.load('Art/spincard/spin_' + str(i) + '.png'), (298.5,495))
            self.card_spin_images.append(self.card_spin_image)

        self.bg_image = pygame.image.load('Art/Ladders_Finish.png')
        self.bg_size = pygame.transform.scale(self.bg_image, (700,700))

    def show(self,row,column,screen,numplay,cat,amount):
        self.row_card = row
        self.column_card = column
        for x in self.chanelcard:
            if self.chanelcard[x][0] == row and self.chanelcard[x][1] == column:
                self.rolling_card = True
                self.randomcard = random.randint(1,6)
                self.rolling(screen,cat,amount)
                print("random card = " + str(self.randomcard-1))
                screen.blit(self.bg_size, (0,0))
                for i in range(amount-1,-1,-1):
                    cat[i].draw(screen)
                screen.blit(self.card_images[self.randomcard-1], (210,110))
                pygame.display.update()
                pygame.time.delay(200)
                if self.randomcard == 1:
                    self.stated_card()
                elif self.randomcard == 2:
                    self.back3chanel()
                elif self.randomcard == 3:
                    self.back5chanel()
                elif self.randomcard == 4:
                    self.forward3chanel()
                elif self.randomcard == 5:
                    self.forward5chanel()
                else:
                    self.stopyourturn(numplay)
                pygame.time.delay(700)
                self.randomcard = 0

    def rolling(self,screen,cat,amount):
        for i in range(18):
            pygame.time.delay(30)
            screen.blit(self.bg_size, (0,0))
            screen.blit(self.card_spin_images[i], (210,110))
            for j in range(amount-1,-1,-1):
                cat[j].draw(screen)
            pygame.display.update()

    def stated_card(self):
        self.row_card = 1
        self.column_card = 1

    def back3chanel(self):
        self.column_card -= 3
        if self.column_card <= 0:
            self.row_card -= 1
            self.column_card = 10 - abs(self.column_card)

    def back5chanel(self):
        self.column_card -= 5
        if self.column_card <= 0:
            self.row_card -= 1
            self.column_card = 10 - abs(self.column_card)

    def forward3chanel(self):
        self.column_card += 3
        if self.column_card > 10:
            self.row_card += 1
            self.column_card -= 10

    def forward5chanel(self):
        self.column_card += 5
        if self.column_card > 10:
            self.row_card += 1
            self.column_card -= 10

    def stopyourturn(self,numplay):
        print("player " + str(numplay + 1) + " has stop 1 turn")
        self.player_stop = numplay

    # ohm dod mai yom tum ghan
    # so alcohol 100% is calling we
    # let's gooooooooooo
    # p'ohm pai siam and pai maid cafe with fern mai giu giu 
    # hur when fern ja dai sleep
    # oke so pround of ohm nsa