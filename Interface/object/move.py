from object.dice import Dice
from object.ladder import LadderSnake
from object.randcard import Card

dice = Dice()
laddersnake = LadderSnake()
card = Card()

def move(cat,amount,screen):
        if dice.randonnum > 0 and not dice.isrolling:
            if cat[dice.numplay].column > 9:
                if cat[dice.numplay].jumpCount >= -12:
                    cat[dice.numplay].y -= (cat[dice.numplay].jumpCount * abs(cat[dice.numplay].jumpCount)) * 0.1
                    cat[dice.numplay].y -= 2.8
                    cat[dice.numplay].jumpCount -= 1
                else:
                    cat[dice.numplay].column = 1
                    cat[dice.numplay].jumpCount = 12
                    cat[dice.numplay].row += 1
                    dice.randonnum -= 1
            else:
                if cat[dice.numplay].jumpCount >= -12:
                    cat[dice.numplay].y -= (cat[dice.numplay].jumpCount * abs(cat[dice.numplay].jumpCount)) * 0.1
                    cat[dice.numplay].jumpCount -= 1
                    if cat[dice.numplay].row % 2 == 0:
                        cat[dice.numplay].x -= 2.8
                    else:
                        cat[dice.numplay].x += 2.8
                else:
                    cat[dice.numplay].jumpCount = 12
                    dice.randonnum -= 1
                    cat[dice.numplay].column += 1
            if dice.randonnum == 0:
                card.show(cat[dice.numplay].row,cat[dice.numplay].column,screen,dice.numplay,cat,amount)
                cat[dice.numplay].row = card.row_card
                cat[dice.numplay].column = card.column_card
                laddersnake.move(cat[dice.numplay].row,cat[dice.numplay].column,screen)
                cat[dice.numplay].row = laddersnake.row_lad
                cat[dice.numplay].column = laddersnake.column_lad
                cat[dice.numplay].y = 623 - ((cat[dice.numplay].row - 1) * 70)
                if cat[dice.numplay].row % 2 == 0:
                    cat[dice.numplay].x = 700 - ((cat[dice.numplay].column) * 70)
                else:
                    cat[dice.numplay].x = 0 + ((cat[dice.numplay].column - 1) * 70)
                dice.numplay += 1
                if dice.numplay > amount - 1:
                    dice.numplay = 0
                if dice.numplay == card.player_stop:
                    dice.numplay += 1
                    card.player_stop = 5
                if dice.numplay > amount - 1:
                    dice.numplay = 0
        else:
            dice.dicing(screen,cat,amount)
        for i in range(amount-1,-1,-1):
            cat[i].draw(screen)