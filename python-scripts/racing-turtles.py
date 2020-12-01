'''
Racing Colored Turtles
22 oct 2017
'''

import random as r
import turtle as t
#import time
#import vlc

def racing_turtles():
    screen = t.getscreen()
    t.bgcolor("grey")
    t.hideturtle()
    racer = list()
    racercolor = ["red","orange","green","blue","pink"]

    # draw race line markers
    t.penup()
    t.goto(t.pos() + ( -450 , 400 ) )
    t.right(90)
    t.pendown()
    t.forward(400)
    
    for marker in range(9):
        t.penup()
        t.goto(t.pos() + ( 100 , 400 ) )
        t.pendown()
        t.forward(400)

    # turtles to starting positions
    for num in range(5):
        racer.append(t.Turtle(shape="turtle"))
        racer[num].penup()
        racer[num].setpos(-450,num*100)
        racer[num].color(racercolor[num])
        
    # start of race
#    p = vlc.MediaPlayer("race-trumpet.mp3")
#    p.play()
#    time.sleep(8)
#    p = vlc.MediaPlayer("cheering.mp3")
#    p.play()
    for rolls in range(50):
        for i in range(5):
            racer[i].forward(r.randint(1,30))
            racer[i].write(i)
    
    t.penup()
    t.goto(t.pos() + ( -500 , 0 ) )
    t.pendown()      
    t.write("CLICK HERE TO CLOSE",font=("Arial",15,"bold"))
    screen.exitonclick()
    
if __name__ == "__main__":
    racing_turtles()
