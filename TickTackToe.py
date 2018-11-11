#Program :  Ticktacktoe.py
#Author : Anthony Merante
#Description : A program that imports data from the Graphics.py File to set up a 3x3 grid and allows users to take turns
#               playing the game until a player wins or a tie occurs.


from Graphics import *

#Set up variables to hold the spots that have been selected.
taken = []
circleSpots = []
xSpots = []
def main():
    # Create a new window, set its coordinates.
    win = GraphWin("Tic-Tac-Toe", 600, 600)
    win.setBackground("grey")
    win.setCoords(0.0, 0.0, 3.0, 3.0) # this sets it from (0,0) lower left to (3,3) upper right)
    #Draw the gameboard
    Line(Point(1,0), Point(1,3)).draw(win)
    Line(Point(2,0), Point(2,3)).draw(win)
    Line(Point(0,1), Point(3,1)).draw(win)
    Line(Point(0,2), Point(3,2)).draw(win)

    while True:
        #Circles Turn
        while True:
            # Get the location of the mouse clicks
            p = win.getMouse()
            x = int(p.getX())
            y = int(p.getY())
            #Check to see if the spot selected is taken
            if (x,y) not in taken:
                taken.append((x,y))
                circleSpots.append((x,y))
                break
            # If spot is selected print message to console informing the user to select another spot
            # TO CONSIDER : Print message on game screen instead?
            else:
                print("Sorry, that spot is taken... Please select a new location.")
        #Draw the circle in the free spot
        cir = Circle(Point(x+.5,y+.5),.5)
        cir.setOutline("black")
        cir.setFill("white")
        cir.draw(win)
        #Check to see if the circle player has won
        if (0,2) in circleSpots and (1,2) in circleSpots and (2,2) in circleSpots:
            print("Circle wins")
            break
        elif (0,1) in circleSpots and (1,1) in circleSpots and (2,1) in circleSpots:
            print("Circle wins")
            break
        elif (0,0) in circleSpots and (1,0) in circleSpots and (2,0) in circleSpots:
            print("Circle wins")
            break
        elif (0,2) in circleSpots and (0,1) in circleSpots and (0,0) in circleSpots:
            print("Circle wins")
            break
        elif (1,2) in circleSpots and (1,1) in circleSpots and (1,0) in circleSpots:
            print("Circle wins")
            break
        elif (2,2) in circleSpots and (2,1) in circleSpots and (2,0) in circleSpots:
            print("Circle wins")
            break
        elif (0,2) in circleSpots and (1,1) in circleSpots and (2,0) in circleSpots:
            print("Circle wins")
            break
        elif (2,2) in circleSpots and (1,1) in circleSpots and (0,0) in circleSpots:
            print("Circle wins")
            break
        #Check to see if the players have tied
        if len(circleSpots + xSpots) == 9:
            print("Both players tied.")
            break
        #X's Turn
        while True:
            p = win.getMouse()
            x = int(p.getX())
            y = int(p.getY())
            if (x,y) not in taken:
                print(x,y)
                taken.append((x,y))
                xSpots.append((x,y))
                break
            else:
                print("That square is taken")
        #Draw the X in the spot selected
        label = Text(Point(x+.5,y+.5),"x")
        label.setSize(126)
        label.draw(win)
        #Check to see if the X player has won
        if (0,2) in xSpots and (1,2) in xSpots and (2,2) in xSpots:
            print("X wins")
            break
        elif (0,1) in xSpots and (1,1) in xSpots and (2,1) in xSpots:
            print("X wins")
            break
        elif (0,0) in xSpots and (1,0) in xSpots and (2,0) in xSpots:
            print("X wins")
            break
        elif (0,2) in xSpots and (0,1) in xSpots and (0,0) in xSpots:
            print("X wins")
            break
        elif (1,2) in xSpots and (1,1) in xSpots and (1,0) in xSpots:
            print("X wins")
            break
        elif (2,2) in xSpots and (2,1) in xSpots and (2,0) in xSpots:
            print("X wins")
            break
        elif (0,2) in xSpots and (1,1) in xSpots and (2,0) in xSpots:
            print("X wins")
            break
        elif (2,2) in xSpots and (1,1) in xSpots and (0,0) in xSpots:
            print("X wins")
            break
    win.getMouse()
    win.close()
main()
