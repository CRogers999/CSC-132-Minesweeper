from Tkinter import *
import random
#from collections import deque

class Minesweeper:

    def __init__(self, master):
        self.tile_plain = PhotoImage(file = "images/tile_plain.gif")


        self.tile_no = []
        for x in range(1, 9):
            self.tile_no.append(PhotoImage(file = "images/tile_"+str(x)+".gif"))



        frame = Frame(master)
        frame.pack()

        self.label1 = Label(frame, text = "Minesweeper")
        self.label1.grid(row = 0, column = 0, columnspan = 10)

        self.buttons = {}
        self.mines = 0
        x_coord = 1
        y_coord = 0
        for x in range(0, 64):
            mine = 0
            gfx = self.tile_plain

            
            # instantiate button, key [x] is called from the previously set dictionary
            self.buttons[x] = [Button(frame, image = gfx),mine,0,x,[x_coord, y_coord], 0]
                                                        
            # calculate coords:
            y_coord += 1
            
            if y_coord == 8:
                y_coord = 0
                x_coord += 1

            print str(x_coord)+ "," +str(y_coord)
            
        # lay buttons in grid
        for x in self.buttons:
            self.buttons[x][0].grid( row = self.buttons[x][4][0], column = self.buttons[x][4][1] )





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
