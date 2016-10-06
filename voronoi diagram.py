from _io import open
from ctypes.wintypes import BOOLEAN
try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True
    
# Examples of mouse input

background_color=['Aquz','Blue','Fuchsia','Gray','Green','Lime','Maroon','Navy','Olive','Orange','Purple','Red','Silver','Teal','Yellow']

import math
import random

# intialize globals
width = 600
height = 600
ball_list = []
ball_radius = 1
ball_color = "BLACK"
i=0

def file_read():
    file = open("test.txt",'r')
    Flag=False;
    global ball_list
    global i
    while True:
        f_str=file.readline()
        #file.readline()
        #print(f_str)
        
        f_list=list(f_str)
#         print(f_str)
        
        if(f_str=="0\n"):
            print(f_str)
            file.close
            break
        elif (f_str=='\n'):
            pass
        elif(f_list[0]!='#'):
            #print(f_str,end='')
            if(Flag==False and int(f_str)>0 ):
                count=int(f_str)
                Flag=True
                
            elif(Flag==True and count):
                pos=f_str.split(' ');
                pos_tu=(int(pos[0]),int(pos[1]))
                print(pos_tu)
                ball_list.append(pos_tu)
                count=count-1
                i+=1
                if(count==0):
                    Flag=False
        else:
            pass    
    
    




# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    ball_list.append(pos)
    print(pos)
    global i
    i+=1
    
#    if distance(ball_pos, pos) < ball_radius:
#        if ball_color == "Red":
#            ball_color = "Green"
#    else:
#        ball_pos = [pos[0], pos[1]]
#        ball_color = "Red"

def draw(canvas):
    global i
    i%=len(background_color)
    for ball_pos in ball_list:
        canvas.draw_circle(ball_pos, ball_radius, 2, "Black", ball_color)
        frame.set_canvas_background(background_color[i])
    
# create frame
frame = simplegui.create_frame("Voronoi Diagram", width, height)
#initial canvas background
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
fileread_button=frame.add_button("File Read(comment)",file_read,200);
# start frame

frame.start()

