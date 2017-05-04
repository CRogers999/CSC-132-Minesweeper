if mine == clicked:
    loseGame()
def loseGame():
    print "Game over"

clickedsquares = 0
if (clickedsquares == (allsquares - minesquares)) or (minesquares == flagged):
    winGame()
def winGame():
    print "You win"
