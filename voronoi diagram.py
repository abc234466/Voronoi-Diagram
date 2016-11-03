"""
#------------------------------------------
# $LAN=Python$
# Author : 陳柏憲  Bo-Xian Chen
# Student ID : M053040020
# Date : 2016/10/05
#------------------------------------------
"""
# [            Voronoi Diagram             ]
from _io import open
from ctypes.wintypes import BOOLEAN
import math
import random
from SimpleGUICS2Pygame.simpleguics2pygame import Canvas
from sympy import * # procress polynomial
from fractions import * #process Fraction

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
line_list = []
ball_radius = 1
ball_color = "BLACK"
start_control = False
i = 0
x = Symbol('x')
y = Symbol('y')

# read file with comment
def read_file_comment():
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

# read file without comment
def read_file():
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

# Write point to file 
def write_file():
    global point_list
    sort_list = sorted(point_list)
    file = open("list.txt", 'w')
    for i in sort_list:
        print (type(i))
        str1 = str(i[0])
        str2 = str(i[1])
        file.write("P " + str1 + " " + str2 + "\n")
    pass

# clear the window
def clear_window():
        global point_list
        point_list = []
        frame.set_canvas_background("White") 
   
# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
        point_list.append(list(pos))
        #print(pos)
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
        global i
        i %= len(color_list)
        for _ in point_list:
            canvas.draw_circle(_, ball_radius, 2, "Black", ball_color)
        #for _ in point_list:    
            #canvas.draw_line([0,0],[600,600],2,"Black")
#             frame.set_canvas_background(color_list[i])
#         canvas.draw_line([0,0], [height,width], 2, color_list[i])

# implement step by step
def step_by_step(canvas):
   pass

def circumcenter(point_ls):
    if(len(point_ls)==2):
        slope = round((point_ls[1][1]-point_ls[0][1])/(point_ls[1][0]-point_ls[0][0]),1) #兩點斜率
        bisetor= 1/slope #
        mid = [(point_ls[1][0]+point_ls[0][0])/2, (point_ls[1][1]+point_ls[0][1])/2] #中點
        print(slope)
        print(bisetor)
        print(mid)
        
    if(len(point_ls)==3):
        print(3)    
# Divide and Conquer
def divide_and_conquer(point):
    print(point)
# Start the Voronoi Diagram
def run():
    divide_and_conquer(point_list)
    circumcenter(point_list)
    
# create frame
frame = simplegui.create_frame("Voronoi Diagram", width, height)

# initial canvas background
frame.set_canvas_background("White")

# register event handler
btm_start = frame.add_button("Run", run, 200);
lable1 = frame.add_label("\n", 1);
btm_start = frame.add_button("Step by step", step_by_step, 200);
lable1 = frame.add_label("\n", 1);
btm_fr_wc = frame.add_button("Read File(comment)", read_file_comment, 200);
lable2 = frame.add_label("\n", 1);
btm_fr_c = frame.add_button("Read File", read_file, 200);
lable4 = frame.add_label("\n", 1);
btm_fr_wf = frame.add_button("Write File", write_file, 200);
lable3 = frame.add_label("\n", 1);

btm_clear = frame.add_button("Clear window", clear_window, 200);

# start frame
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.start()
