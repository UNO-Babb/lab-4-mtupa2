#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS


def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360 / sides)

def fillCorner(alice, corner):
    # Draw big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        alice.backward(50)
    elif corner == 3:
        alice.forward(50)
        alice.right(90)
        alice.forward(100)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        alice.backward(100)
        alice.left(90)
        alice.backward(50)
    elif corner == 4:
        alice.forward(100)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        alice.backward(100)

def drawConcentricSquares(myTurtle, start_size, count, step):
    size = start_size
    for _ in range(count):
        drawSquare(myTurtle, size)
        myTurtle.penup()
        myTurtle.forward(step / 2)
        myTurtle.right(90)
        myTurtle.forward(step / 2)
        myTurtle.left(90)
        myTurtle.pendown()
        size -= step * 2

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(5)
    t.pensize(2)
    
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    
    drawConcentricSquares(t, 300, 6, 20)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
