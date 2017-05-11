from constellations import *

from Tkinter import *
import random
import tkMessageBox

global x_input
global y_input
global count
count = 1
x_input = 1
y_input= 0    

   

class Skysweeper:

    def __init__(self, master):
        #create frame window
        global window
        window = Frame(height = 32, width = 32, bg= "black")
        window.pack()

        #images being used in GUI 
        self.tile_plain = PhotoImage(file = "images/tile_plain.gif")
        self.tile_clicked = PhotoImage(file = "images/my_sky.gif")
        self.tile_mine = PhotoImage(file = "images/gold_star.gif")
        self.tile_flag = PhotoImage(file = "images/tile_flag.gif")
        self.tile_wrong = PhotoImage(file = "images/tile_wrong.gif")
        self.title = PhotoImage(file = "images/title.gif")
        self.flags_text = PhotoImage(file = "images/flags_text.gif")
        self.mine_text = PhotoImage(file = "images/mine_text.gif")
        self.level_text = PhotoImage(file = "images/level_text.gif")
  
        #sets up images for values displayed at bottom of grid
        self.numbers = []
        for x in range (0,11):   
            self.numbers.append(PhotoImage(file = "images/"+str(x)+".gif")) 
             

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
       
        #labels for GUI aesthetics  
        self.label4 = Label(window, image = self.level_text)
        self.label3 = Label(window, image = self.flags_text)
        self.label2 = Label(window, image = self.mine_text)
        self.label_title = Label(window, image = self.title)
        

        #where logic for grid layout begins
        if count == 1:
            self.grid_1(144)
            
        if count == 2:
            self.grid_2(225)

        if count == 3:
            pass


        # lay buttons in grid
        for x in self.tiles:
            self.tiles[x][0].grid( row = self.tiles[x][4][0], column = self.tiles[x][4][1] )

        #button for resetting game
        b = Button(window, text = "Reset", command = self.callback)
        b.grid(row = 6, column = 12, columnspan = 1, sticky = "")
        self.nearbyMines()
        print "#####################################################"
        self.cheat()

    def callback(self):
        sys.exit
        game.destroy()
        main()
        
    # end of init
    def pick(self):
        global picked
        large_constellations = []
        small_constellations = {"Leo":Leo(x_input,y_input),
                                "Libra": Libra(x_input,y_input),
                                "Cancer":Cancer(x_input,y_input),
                                "Capricorn":Capricorn(x_input,y_input)}
        small_constellations.keys()
        picked = random.choice(small_constellations.keys())
        print picked
            
        

    def grid_1(self,value):
        self.pick()
        x_input = 1
        y_input = 0
        global mine
        self.label_title.grid(row = 0, column = 0, columnspan = 12) 
        #startup()
        #loop that creates grid based upon size of range
        for x in range (value):
                mine = 0
                default_img = self.tile_plain
                #constellation placement
                if picked == "Libra":
                    if Libra(x_input,y_input):
                        mine = 1
                        self.mines += 1

                if picked == "Cancer":
                    if Cancer(x_input,y_input):
                        mine = 1
                        self.mines += 1

                if picked == "Leo":
                    if Leo(x_input,y_input):
                        mine = 1
                        self.mines += 1
                if picked == "Capricorn":
                    if Capricorn(x_input,y_input):
                        mine = 1
                        self.mines += 1    
                    
                #Keys:
                    #0 button widget
                    #1 mine (1 = yes , 0 = no)
                    #2 state 0 = unclicked, 1 = clicked, 2 = flagged)
                    #3 button id
                    #4 [x, y] coords
                    #5 nearby mines
                # instantiate button, x [x] is called from the previously set dictionary
                self.tiles[x] = [Button(window, image = default_img),mine,0,x,[x_input, y_input], 0]
                self.tiles[x][0].bind('<Button-1>',self.leftClick_wrapper(x))
                self.tiles[x][0].bind('<Button-3>',self.rightClick_wrapper(x))


                # calculate coords:
                y_input += 1
                if y_input == 12:
                    y_input = 0
                    x_input += 1
                #print str(x)+": "+str(x_input)+ "," +str(y_input)

           
        self.label_info3 = Label(window, image = self.numbers[count])
        self.label_info2 = Label(window, image = self.numbers[self.flags])
        self.label_info1 = Label(window, image = self.numbers[self.mines])        

        #bottom of GUI (mines, flags, level)
        #number of mines displayed
        self.label2.grid(row = 20, column = 0, columnspan = 3, sticky = W)
        self.label_info1.grid(row = 20, column = 3 , columnspan =3, sticky = W)
                            

        #number of flags displayed
        self.label3.grid(row = 20, column = 4, columnspan = 3, sticky = W)
        self.label_info2.grid(row = 20, column = 7, columnspan = 3, sticky = W)

        
        #level displayed
        self.label4.grid(row = 20, column = 8, columnspan = 3, sticky = E)
        self.label_info3.grid(row = 20, column = 10, columnspan = 3, sticky = "")



    def grid_2(self,value):
        x_input = 1
        y_input= 0 
        self.label_title.grid(row = 0, column = 0, columnspan = 20, sticky = "")
            #loop that creates grid based upon size of range
        for x in range (value):
                mine = 0
                default_img = self.tile_plain
            
                if x_input == 10 and y_input == 1:
                    mine = 1
                    self.mines += 1
                if x_input == 2 and y_input == 14:
                    mine = 1
                    self.mines += 1
                if x_input == 8 and y_input == 8:
                    mine = 1
                    self.mines += 1
                if x_input == 12 and y_input == 3:
                    mine = 1
                    self.mines += 1
                if x_input == 5 and y_input == 9:
                    mine = 1
                    self.mines += 1
                if x_input == 9 and y_input == 12:
                    mine = 1
                    self.mines += 1
                if x_input == 3 and y_input == 1:
                    mine = 1
                    self.mines += 1
                if x_input == 11 and y_input == 15:
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
                self.tiles[x] = [Button(window, image = default_img),mine,0,x,[x_input, y_input], 0]
                self.tiles[x][0].bind('<Button-1>',self.leftClick_wrapper(x))
                self.tiles[x][0].bind('<Button-3>',self.rightClick_wrapper(x))


                # calculate coords:
                y_input += 1
                if y_input == 15:
                    y_input = 0
                    x_input += 1
               # print str(x)+": "+str(x_input)+ "," +str(y_input)




        #sets up bottom images
        #sets up images for values displayed at bottom of grid
        self.label_info3 = Label(window, image = self.numbers[count])
        self.label_info2 = Label(window, image = self.numbers[self.flags])
        self.label_info1 = Label(window, image = self.numbers[self.mines]) 
    
  

        #bottom of GUI (mines, flags, level)
        #number of mines displayed
        self.label2.grid(row = 20, column = 0, columnspan = 4, sticky = W)
        self.label_info1.grid(row = 20, column = 3 , columnspan =2, sticky = W)
                            

        #number of flags displayed
        self.label3.grid(row = 20, column = 5, columnspan = 3, sticky = "")
        self.label_info2.grid(row = 20, column = 8, columnspan = 2, sticky = W)

        
        #level displayed
        self.label4.grid(row = 20, column = 10, columnspan = 4, sticky = E)
        self.label_info3.grid(row = 20, column = 14, columnspan = 2, sticky = E)








    def rightClick_wrapper(self, x):
        return lambda Btn: self.rightClick(self.tiles[x])

    def leftClick_wrapper(self, x):
        return lambda Btn: self.leftClick(self.tiles[x])

    def leftClick(self, btn):
        print str(btn[3])+ ": "+ str(btn[4])+ "nearby mines = "+str(btn[5])
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
            #self.check_win()

            
    def rightClick(self, btn):
        print str(btn[3])+ ": "+ str(btn[4])+ "nearby mines = "+str(btn[5])
        # if not clicked
        if btn[1] == 1:
            btn[0].config(image = self.tile_flag)
        if btn[2] == 0:
            btn[0].config(image = self.tile_flag)
            btn[2] = 2
           
            # if a mine
            if btn[1] == 1:
                self.correct += 1
            self.flags += 1
            self.label_info2.config(image = self.numbers[self.flags]) 
            self.updateFlags()

        # remove flag
        elif btn[2] == 2:
            btn[0].config(image = self.tile_plain)
            btn[2] = 0
            
            # if removing flag from a mine
            if btn[1] == 1:
                self.correct -= 1
            self.flags -= 1
            self.label_info2.config(image = self.numbers[self.flags]) 
            self.updateFlags()
        print self.correct
        #self.check_win()

    def updateFlags(self):
        self.label3.config(text = "Flags: " +str(self.flags))
     
    def check_mines(self, x):
        try:
            if self.tiles[x][1] == 1:
                return True
        except KeyError:
            pass

    #checks each button for mines near it and totals it in the nearbymines variable
    #+13 +12 +11    
    #+1   x  -1
    #-11 -12 -13
    #visual representation of checking     
    def nearbyMines(self):     
        if count == 1:
            for x in self.tiles:
                nearbymines = 0
                check_area = self.tiles[x][3]
                check_area = [(x+13),(x+12),(x+11),(x+1),(x-1),(x-11),(x-12),(x-13)]
                for i in range(len(check_area)):
                    if self.check_mines(check_area[i]):
                        nearbymines += 1

                #update each tile with amount of mines near it
                self.tiles[x][5] = nearbymines
        
        if count == 2:
            for x in self.tiles:
                nearbymines = 0
                check_area = self.tiles[x][3]
                check_area = [(x+16),(x+15),(x+14),(x+1),(x-1),(x-14),(x-15),(x-16)]    
                for i in range(len(check_area)):
                    if self.check_mines(check_area[i]):
                        nearbymines += 1

                #update each tile with amount of mines near it
                self.tiles[x][5] = nearbymines  

    #takes x value from self.tiles
    def checkTile(self,x, keys):
        try:     
            if self.tiles[x][2] == 0:
                if self.tiles[x][5] == 0 and self.tiles[x][1] == 0:
                    self.tiles[x][0].config(image = self.tile_clicked)
                    keys.append(x)
                    self.clicked += 1

            elif self.tiles[x][5] > 0 and self.tiles[x][1] == 0:
                self.tiles[x][0].config(image = self.tile_num[self.tiles[x][5]-1])
                self.clicked+= 1

            self.tiles[x][2] = 1
        except KeyError:
            pass

    def clearTiles(self,x):
        keys = [x]
        for x in keys:
            self.checkTile(x+11, keys)     #top right
            self.checkTile(x+12, keys)     #top middle
            self.checkTile(x+13, keys)     #top left
            self.checkTile(x+1, keys)      #left
            self.checkTile(x-1, keys)      #right
            self.checkTile(x-13, keys)     #bottom right
            self.checkTile(x-12, keys)     #bottom middle
            self.checkTile(x-11, keys)     #bottom left


    def loseGame(self):
        for x in self.tiles:
            self.clearTiles(self.tiles[x][3])
        #message = tkMessageBox.askyesno(title="Game Over!", message="Play again?")
        #if message == True:
        #    print "yay"
        #    sys.exit
        #    game.destroy()
       #     main()
       #         
       # else:
        #   game.destroy() 
        
        
    def winGame(self):
        levelCount()
        for x in self.tiles:
            self.clearTiles(self.tiles[x][3])
        print "You win!"
        window2 = tkMessageBox.askyesno(title="You Win!", message= "Continue?")
        if window2 == True:
            sys.exit
            game.destroy()
            main()
        else:
            game.destroy()

    def check_win(self):
        if count == 1:
            if self.correct == self.mines or self.clicked == 144-self.mines: 
                self.winGame()
        if count == 2:
            if self.correct == self.mines or self.clicked == 225-self.mines:
                self.winGame()

    def cheat(self):
      for x in self.tiles:
          #self.clearTiles(self.tiles[x][3])
          if self.tiles[x][1] == 1:
              self.tiles[x][0].config(image = self.tile_mine)
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
    
def startup():
    tkMessageBox.showinfo( title = "Welcome to Skysweeper", message = ("Left click to reveal squares. Right click to place flags. The game is lost if a mine is clicked. The game is won if there are flags on all mines."))



main()



