from Tkinter import *
import random
#from collections import deque

class Minesweeper:

    def __init__(self, master):
        self.tile_plain = PhotoImage(file = "images/tile_plain.gif")


        #self.tile_no = []
        #for x in range(1, 9):
        #    self.tile_no.append(PhotoImage(file = "images/tile_"+str(x)+".gif"))



        frame = Frame()
        frame.pack()

        self.label1 = Label(frame, text = "Minesweeper")
        self.label1.grid(row = 0, column = 0, columnspan = 8)

        self.buttons = {}
        x_input = 1
        y_input= 0
        for x in range(0, 64):
            mine = 0
            img = self.tile_plain

            #reword 
            # instantiate button, key [x] is called from the previously set dictionary
            self.buttons[x] = [Button(frame, image = img),mine,0,x,[x_input, y_input], 0]
                                                        
            # calculate coords:
            y_input += 1
            
            if y_input == 8:
                y_input = 0
                x_input += 1

            print str(x_input)+ "," +str(y_input)
            
        # lay buttons in grid
        for x in self.buttons:
            self.buttons[x][0].grid( row = self.buttons[x][4][0], column = self.buttons[x][4][1] )


    #need to add mines outside of init i think, or else the class would have to be repeatedly instantiated
    def addMines():

    
def main():
    global game
    #create Tk widget
    game = Tk()
    #set program title
    game.title("Minesweeper")
    #create game instance
    minesweeper = Minesweeper(game)
    game.mainloop()


main()