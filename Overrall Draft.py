#import all the needed libraries
from Tkinter import *
from random import randint



##Designs the interactive window: the grid itself, the undifferentiated squares(tiles),
  #their input, the buttons that cover the tiles,
class Grid(Canvas):
    #Constructor
    def __init__(self, master):
        Canvas.__init__(self, master, bg = "white")
        self.pack(fill = BOTH, expand = 1)


    #calls all the functions that occur below it to setup the GUI within the Grid class
    def setupGUI():
        self.tiles()
        self.constellation()
        self.buttons()
        pass
    
    #creates the tiles depending on the width and height
    def tiles(self):
        pass

    #randomly picks a constellation to put into the tiles
    #inserts both the mines and the numbers around it
    def constellation(self):
        pass

    #creates the buttons that hide the contents of the tiles
    def buttons(self):
        pass
    
    #reveals the tile's contents when prompted
    #*Next item of concern*#
    def reveal(self):
        pass
    
    #inserts flags when prompted
    def flag(self):
        pass
    
    

##class Minesweeper(Grid):
#contains all the functions initialized while the game is played
def play(self):
    #create the window
    window = Tk()
    window.geometry("{}x{}".format(WIDTH, HEIGHT))
    windom.title("The Minesweeper Game")
    

    #create the grid as a Tkinter canvas inside the window
    m = Grid(window)

    #*To ba added later*#
    #Width and Height increase with difficulty
    #WIDTH =
    #HEIGHT =
    
    #configures the Grid as a GUI
    #Is dependent on the size of the grid
    m.setupGUI()

    ##To be added later
    #adds timer to the game
    m.timer()
    #displays hint on LED
    m.led()
    #plays the sound
    m.sound()
    #allows the player to play again
    m.life()
    

    #waits for the window to close
    window.mainloop()



#Defines what happens when the player loses
def loseGame(self):
    pass

#Defines what happens when the player wins
def winGame(self):
    pass



#*To be added later*#
#Increments the time when the game begins
def timer(self):
    pass

#plays a sound when the game is won or lost
def sound(self):
    pass

#displays a hint on LEDS
def led(self):
    pass

def life(self):
    pass

##class *(Frame): ###See room adventure's use of frame or replace grid with scoreboard
#displays the scores and ranks at the end of each level
def scoreboard(self):
    pass


#################################################################################################
#START THE GAME!!!



