from Tkinter import *
import random
import tkMessageBox
from collections import deque
import RPi.GPIO as GPIO
import pygame

pygame.init()

#establishes which pins go to which colors
white = [26]
red = [5, 6, 13, 19]
yellow = [12, 16, 20, 21]
green = [23, 24]

GPIO.setmode(GPIO.BCM)

#sets the pins
GPIO.setup(white, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

global count
count = 0

class Skysweeper:

    def __init__(self, master):
        #create frame window
        global window
        window = Frame()
        window.pack()
        #title at top of GUI
        self.label1 = Label(window, text = "Skysweeper")
        self.label1.grid(row = 0, column = 0, columnspan = 8)
        #images being used in GUI 
        self.tile_plain = PhotoImage(file = "images/tile_plain.gif")
        self.tile_clicked = PhotoImage(file = "images/tile_clicked.gif")
        self.tile_mine = PhotoImage(file = "images/tile_mine.gif")
        self.tile_flag = PhotoImage(file = "images/tile_flag.gif")
        self.tile_wrong = PhotoImage(file = "images/tile_wrong.gif")

        #used for numbers on tiles for mine proximity
        self.tile_num = []
        for x in range(1, 9):
            self.tile_num.append(PhotoImage(file = "images/tile_"+str(x)+".gif"))
        
        #variables for win conditions
        self.level = count
        self.flags = 0
        self.correct = 0
        self.clicked = 0

        
        #variables for button and mine placement 
        self.mines = 0
        self.tiles = {}
        global x_input
        global y_input
        x_input = 1
        y_input= 0    
        #loop that creates grid based upon size of range
        for x in range(1, 101):
            mine = 0
            img = self.tile_plain
            #random amount of mines
            if random.uniform(0.0 , 1.5) < 0.15:
                mine = 1
                self.mines += 1
            #Keys:
                #0 button widget
                #1 mine (1 = yes , 0 = no)
                #2 state 0 = unclicked, 1 = clicked, 2 = flagged)
                #3 button id
                #4 [x, y] coords
                #5 nearby mines
            # instantiate button, key [x] is called from the previously set dictionary
            self.tiles[x] = [Button(window, image = img),mine,0,x,[x_input, y_input], 0]
            self.tiles[x][0].bind('<Button-1>',self.leftClick_wrapper(x))
            self.tiles[x][0].bind('<Button-3>',self.rightClick_wrapper(x))


            # calculate coords:
            y_input += 1
            if y_input == 10:
                y_input = 0
                x_input += 1
            print str(x)+": "+str(x_input)+ "," +str(y_input)
            

        # lay buttons in grid
        for x in self.tiles:
            self.tiles[x][0].grid( row = self.tiles[x][4][0], column = self.tiles[x][4][1] )

        
        self.nearbyMines()

        self.label2 = Label(window, text = "Mines: "+str(self.mines))
        self.label2.grid(row = 15, column = 0, columnspan = 5)

        self.label3 = Label(window, text = "Flags: "+str(self.flags))
        self.label3.grid(row = 15, column = 4, columnspan = 5)

        self.label4 = Label(window, text = "Level: "+str(count))
        self.label4.grid(row = 15, column = 8, columnspan = 4)
        print "#####################################################"
        #self.cheat()
        
    # end of init
   
       

    def rightClick_wrapper(self, x):
        return lambda Btn: self.rightClick(self.tiles[x])

    def leftClick_wrapper(self, x):
        return lambda Btn: self.leftClick(self.tiles[x])

    def leftClick(self, btn):
        print str(btn[3])+ ": "+ str(btn[4])
        if btn[1] == 1: #if a mine
            # show all mines and check for flags
            for x in self.tiles:
                if self.tiles[x][1] != 1 and self.tiles[x][2] == 2:
                    self.tiles[x][0].config(image = self.tile_wrong)
                if self.tiles[x][1] == 1 and self.tiles[x][2] != 2:
                    self.tiles[x][0].config(image = self.tile_mine)
                # end game
            self.loseGame()
        else:
            #change image
            if btn[5] == 0:
                btn[0].config(image = self.tile_clicked)
                self.clearTiles(btn[3])
            else:
                btn[0].config(image = self.tile_num[btn[5]-1])
            # if not clicked, change to clicked. Then increment counter until player wins/loses
            if btn[2] != 1:
                btn[2] = 1
                self.clicked += 1
            if self.clicked == 100 - self.mines:
                self.winGame()

    def rightClick(self, btn):
        print self.correct
        # if not clicked
        if btn[2] == 0:
            btn[0].config(image = self.tile_flag)
            btn[2] = 2
           
            # if a mine
            if btn[1] == 1:
                self.correct += 1
            self.flags += 1
            self.updateFlags()

        # remove flag
        elif btn[2] == 2:
            btn[0].config(image = self.tile_plain)
            btn[2] = 0
            
            # if removing flag from a mine
            if btn[1] == 1:
                self.correct -= 1
            self.flags -= 1
            self.updateFlags()

    def updateFlags(self):
        self.label3.config(text = "Flags: " +str(self.flags))
     
    def check_mines(self, x):
        try:
            if self.tiles[x][1] == 1:
                return True
        except KeyError:
            pass

    #checks each button for mines near it and totals it in the nearbymines variable
    #L1 M1 R1    
    #L2 x  R2
    #L3 M2 R3
    #visual representation of checking     
    def nearbyMines(self):     
        for x in self.tiles:
            nearbymines = 0
            
            if self.check_mines(x-9):  #top left
                nearbymines += 1
            
            if self.check_mines(x-10): #top 
                nearbymines += 1

            if self.check_mines(x-11): #top right
                nearbymines += 1

            if self.check_mines(x-1):  #left
                nearbymines += 1

            if self.check_mines(x+1):  #right
                nearbymines += 1

            if self.check_mines(x+9):  #bottom left
                nearbymines += 1

            if self.check_mines(x+10): #bottom middle
                nearbymines += 1

            if self.check_mines(x+11): #bottom right 
                nearbymines += 1

            self.tiles[x][5] = nearbymines



    def checkTile(self,key, queue):
        try:     
            if self.tiles[key][2] == 0:
                if self.tiles[key][5] == 0 and self.tiles[key][1] == 0:
                    self.tiles[key][0].config(image = self.tile_clicked)
                    queue.append(key)

            elif self.tiles[key][5] > 0 and self.tiles[key][1] == 0:
                self.tiles[key][0].config(image = self.tile_num[self.tiles[key][5]-1])

            self.tiles[key][2] = 1
            self.clicked += 1
        except KeyError:
            pass

    def clearTiles(self,main_key):
        queue = deque([main_key])

        while len(queue) != 0:
            key = queue.popleft()
            self.checkTile(key-9, queue)      #top right
            self.checkTile(key-10, queue)     #top middle
            self.checkTile(key-11, queue)     #top left
            self.checkTile(key-1, queue)      #left
            self.checkTile(key+1, queue)      #right
            self.checkTile(key+9, queue)      #bottom right
            self.checkTile(key+10, queue)     #bottom middle
            self.checkTile(key+11, queue)     #bottom left
    
    
    
    def loseGame(self):
        try:
            while (True):
        
                GPIO.output(white, True)#turns the white led on
                sleep(0.5)
                GPIO.output(white, False)#turns the white led off
                GPIO.output(red, True)#turns the red led on
                sleep(0.5)
                GPIO.output(red, False)#turns the red leds off
                GPIO.output(yellow, True)#turns the yellow leds on
                sleep(0.5)
                GPIO.output(yellow, False)#turns the yellow leds off
                GPIO.output(green, True)#turns the green leds on
                sleep(0.5)
                GPIO.output(green, False)#turns the green leds off

        except KeyboardInterrupt:
            GPIO.cleanup()
            
        for x in self.tiles:
            self.clearTiles(self.tiles[x][3])
        print "Game over!"
        #game.destroy()
        #main()
        message = tkMessageBox.askyesno(title="Game Over!", message="Play again?")
        if message == True:
            print "yay"
            sys.exit
            game.destroy()
            main()
                
        else:
           game.destroy() 
        
        
    def winGame(self):
        levelCount()
        print "You win!"
        sys.exit
        game.destroy()
        main()

    def cheat(self):
      for x in self.tiles:
          self.clearTiles(self.tiles[x][3])

def main():
    global game
    #create Tk widget
    game = Tk()
    #set program title
    game.title("Minesweeper")
    #create game instance
    skysweeper = Skysweeper(game)
    game.mainloop()

def levelCount():
     global count
     count += 1
    


main()
