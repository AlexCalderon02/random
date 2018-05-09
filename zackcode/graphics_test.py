from graphics import *

#Main function to enter information for the program to process to make the graph
def main():
    #h = input("Enter the height: ")
    #w = input("Enter the width: ")
    graph()

def graph(): #This function draws the basic graph to be graphed on
    length = 500
    height = 500
    center = Point(length/2, height/2)
    lineColor = "white"
    backgroundColor = "black"
    win = GraphWin("Sinewave", length, height) #Takes the users input to size the graph
    win.setBackground(backgroundColor)
    ptVert1 = Point(height/2, height) #No matter what the input, the axis lines are always centered
    ptVert2 = Point(height/2, 0)
    ptHorz1 = Point(length, height/2)
    ptHorz2 = Point(0, height/2)
    lineVert = Line(ptVert1, ptVert2) #Drawing the horizontal and vertical lines from
    lineHorz = Line(ptHorz1, ptHorz2) #the two points created for each line.
    lineVert.setOutline(lineColor)
    lineVert.draw(win)
    lineHorz.setOutline(lineColor)
    lineHorz.draw(win)
    horztempx = length/2 + 5
    horztempy = height - height
    _horztempx = horztempx
    verttempy = height/2 + 5
    verttempx = length - length
    _verttempy = verttempy
    for i in range(0, 100): #Eventual tick marks to represent intervals of 5 on the graph
        #horztempx = length/2
        #horztempy = height/2
        #horztempx += 5
        horztempy += 10
        horztickMarkpoint1 = Point(horztempx, horztempy)
        horztempx -= 11
        horztickMarkpoint2 = Point(horztempx, horztempy)
        horztickmark = Line(horztickMarkpoint1, horztickMarkpoint2)
        horztickmark.setOutline(lineColor)
        horztickmark.draw(win)
        horztempx = _horztempx

        #Draws tick marks Vertically
        verttempx += 10
        verttickMarkpoint1 = Point(verttempx, verttempy)
        verttempy -= 11
        verttickMarkpoint2 = Point(verttempx, verttempy)
        verttickmark = Line(verttickMarkpoint1, verttickMarkpoint2)
        verttickmark.setOutline(lineColor)
        verttickmark.draw(win)
        verttempy = _verttempy
    win.getMouse()
    win.close()

main()




