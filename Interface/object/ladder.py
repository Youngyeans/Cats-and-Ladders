import pygame

class LadderSnake(object):
    def __init__(self):
        self.chanel = {
            #index 0,1 is row and column where cat stand
            #index 2,3 is row and column where cat move to
            #ladders
            'ch4' : [1,4,3,5],
            'ch13' : [2,3,5,6],
            'ch33' : [4,3,5,9],
            'ch42' : [5,2,7,3],
            'ch50' : [5,10,7,9],
            'ch62' : [7,2,9,1],
            'ch74' : [8,4,10,2],
            #snake
            'ch27' : [3,7,1,5],
            'ch40' : [4,10,1,3],
            'ch43' : [5,3,2,8],
            'ch54' : [6,4,4,1],
            'ch66' : [7,6,5,5],
            'ch76' : [8,6,6,8],
            'ch89' : [9,9,6,3],
            'ch99' : [10,9,5,1]
        }
        self.row_lad = 1
        self.column_lad = 1

    def move(self,row,column,screen):
        self.row_lad = row
        self.column_lad = column
        for x in self.chanel:
            if self.chanel[x][0] == row and self.chanel[x][1] == column:
                self.row_lad = self.chanel[x][2]
                self.column_lad = self.chanel[x][3]