import pygame
from Randcard import randcard

class LadderSnake(object):
    def __init__(self):
        self.chanel = {
            #index 0,1 is row and column where cat stand
            #index 2,3 is row and column where cat move to
            #ladders
            'ch4' : [1,4,3,5],
            'ch13' : [2,3,5,6],
            'ch33' : [4,3,5,9],
            'ch42' : [5,2,7,8],
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
            'ch99' : [10,9,5,1],
        }
        self.chanel.back3 = {
            #back3
            'ch10' : [1,10,1,7],
            'ch15' : [2,5,2,2],
            'ch20' : [2,10,2,7],
            'ch29' : [3,9,3,6],
            'ch37' : [4,7,4,4],
            'ch52' : [6,2,5,9],
            'ch56' : [6,6,6,3],
            'ch61' : [7,1,6,7],
            'ch71' : [8,1,7,7],
            'ch77' : [8,7,8,4],
            'ch86' : [9,6,9,3],
            'ch93' : [10,3,9,10],
            'ch98' : [10,8,10,5]
        }
        self.chanel.back5 = {
            #back5
            'ch10' : [1,10,1,5],
            'ch15' : [2,5,1,10],
            'ch20' : [2,10,2,5],
            'ch29' : [3,9,3,6],
            'ch37' : [4,7,4,2],
            'ch52' : [6,2,5,7],
            'ch56' : [6,6,6,1],
            'ch61' : [7,1,6,5],
            'ch71' : [8,1,7,5],
            'ch77' : [8,7,8,2],
            'ch86' : [9,6,9,1],
            'ch93' : [10,3,9,8],
            'ch98' : [10,8,10,3]
        }
        self.chanel.forward3 = {
            #forward3
            'ch10' : [1,10,2,3],
            'ch15' : [2,5,2,8],
            'ch20' : [2,10,3,3],
            'ch29' : [3,9,4,2],
            'ch37' : [4,7,4,10],
            'ch52' : [6,2,6,5],
            'ch56' : [6,6,6,9],
            'ch61' : [7,1,7,4],
            'ch71' : [8,1,8,4],
            'ch77' : [8,7,8,10],
            'ch86' : [9,6,9,9],
            'ch93' : [10,3,10,6],
            'ch98' : [10,8,10,10]
        }
        self.chanel.forward5 = {
            #forward5
            'ch10' : [1,10,2,5],
            'ch15' : [2,5,2,10],
            'ch20' : [2,10,3,5],
            'ch29' : [3,9,4,4],
            'ch37' : [4,7,5,2],
            'ch52' : [6,2,6,7],
            'ch56' : [6,6,7,1],
            'ch61' : [7,1,7,6],
            'ch71' : [8,1,8,6],
            'ch77' : [8,7,9,2],
            'ch86' : [9,6,10,1],
            'ch93' : [10,3,10,8],
            'ch98' : [10,8,10,10]
        }
        self.chanel.start = {
            #start
            'ch10' : [1,10,0,0],
            'ch15' : [2,5,0,0],
            'ch20' : [2,10,0,0],
            'ch29' : [3,9,0,0],
            'ch37' : [4,7,0,0],
            'ch52' : [6,2,0,0],
            'ch56' : [6,6,0,0],
            'ch61' : [7,1,0,0],
            'ch71' : [8,1,0,0],
            'ch77' : [8,7,0,0],
            'ch86' : [9,6,0,0],
            'ch93' : [10,3,0,0],
            'ch98' : [10,8,0,0]
        }
        self.row_lad = 1
        self.column_lad = 1
        self.randcard = randcard()
        self.randcard.show()

    def move(self,row,column):
        self.row_lad = row
        self.column_lad = column
        if self.randcard.text == "back3":
            self.chanel = self.chanel.back3
        elif self.randcard.text == "back5":
            self.chanel = self.chanel.back5
        elif self.randcard.text == "forward3":
            self.chanel = self.chanel.forward3
        elif self.randcard.text == "forward5":
            self.chanel = self.chanel.forward5
        elif self.randcard.text == "stop":
            self.chanel = self.chanel.stop
        for x in self.chanel:
            if self.chanel[x][0] == row and self.chanel[x][1] == column:
                self.row_lad = self.chanel[x][2]
                self.column_lad = self.chanel[x][3]
