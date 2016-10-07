#
# Written by Bo-Xian Chen From 2016/10/05
#
#---------------Begin----------------------
from _io import open
from ctypes.wintypes import BOOLEAN
import math
import random


try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True
    
# Examples of mouse input

color_list = ['Aquz', 'Blue', 'Fuchsia', 'Gray', 'Green', 'Lime', 'Maroon', 'Navy', 'Olive', 'Orange', 'Purple', 'Red', 'Silver', 'Teal', 'Yellow']


# intialize globals
width = 600
height = 600
point_list = []
ball_radius = 1
ball_color = "BLACK"
start_control = False
i = 0

def file_read_comment():
    if(start_control == True):
        file = open("test.txt", 'r')
        Flag = False;
        global point_list
        global i
        while True:
            f_str = file.readline()
            # file.readline()
            # print(f_str)
        
            f_list = list(f_str)
            print(f_str)
        
            if(f_str == "0\n"):
#             print(f_str)
                file.close
                break
            elif (f_str == '\n'):
                continue
            elif(f_list[0] != '#'):
                # print(f_str,end='')
                if(Flag == False and int(f_str) > 0):
                    count = int(f_str)
                    Flag = True
                
                elif(Flag == True and count):
                    pos = f_str.split(' ');
                    pos_ls = list((int(pos[0]), int(pos[1])))
#                     print(pos_ls)
                    point_list.append(pos_ls)
                    count = count - 1
                    i += 1
                if(count == 0):
                    Flag = False
            else:
                pass    
    
def file_read():
    if(start_control == True):
        file = open("test2.txt", 'r')
        Flag = False;
        global point_list
        global i
        while True:
            f_str = file.readline()
        # file.readline()
        # print(f_str)
        
            f_list = list(f_str)
#             print(f_str)
        
            if(f_str == "0"):
#             print(f_str)
                file.close
                break
            elif (f_str == '\n'):
                continue
            elif(f_list[0] != '#'):
            # print(f_str,end='')
                if(Flag == False and int(f_str) > 0):
                    count = int(f_str)
                    Flag = True
                
                elif(Flag == True and count):
                    pos = f_str.split(' ');
                    pos_ls = list((int(pos[0]), int(pos[1])))
                    print(pos_ls)
                    point_list.append(pos_ls)
                    count = count - 1
                    i += 1
                    if(count == 0):
                        Flag = False
            else:
                pass

#Write the file
def write_file():
    global point_list
    sort_list=sorted(point_list)
    file = open("list.txt", 'w')
    for i in sort_list:
        print (i)
        str1=str(i[0])
        str2=str(i[1])
        file.write("P "+str1+" "+str2+"\n")
    pass

# clear the window
def clear_window():
    if(start_control == True):
        global point_list
        point_list = []
        frame.set_canvas_background("White") 
   
# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
    if(start_control == True):
        point_list.append(pos)
        print(pos)
        global i
        i += 1
    
#    if distance(point, pos) < ball_radius:
#        if ball_color == "Red":
#            ball_color = "Green"
#    else:
#        point = [pos[0], pos[1]]
#        ball_color = "Red"

# Draw the canvas 
def draw(canvas):
    if(start_control == True):
        global i
        i %= len(color_list)
        for point in point_list:
            canvas.draw_circle(point, ball_radius, 2, "Black", ball_color)
#             frame.set_canvas_background(color_list[i])
        if(len(point_list)>0):
            divide_and_Conquer(point_list)
#         canvas.draw_line([0,0], [height,width], 2, color_list[i])
            
#Divide and Conquer
def divide_and_Conquer(pos):
    print(pos)
# Start the Voronoi Diagram
def start():
    global start_control
    frame.set_mouseclick_handler(click)
    frame.set_draw_handler(draw)
    start_control = True
    
# create frame
frame = simplegui.create_frame("Voronoi Diagram", width, height)

# initial canvas background
frame.set_canvas_background("White")

# register event handler
btm_start = frame.add_button("Start", start, 200);
btm_fr_wc = frame.add_button("Read File(comment)", file_read_comment, 200);
btm_fr_wf = frame.add_button("Write File", write_file, 200);

btm_fr_c = frame.add_button("Read File", file_read, 200);
btm_clear = frame.add_button("Clear window", clear_window, 200);

# start frame

frame.start()
