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
from fractions import *  # process Fraction
import math
import random
from SimpleGUICS2Pygame.simpleguics2pygame import Canvas
from sympy import *  # procress polynomial


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
point_begin = 0
point_end = 0
ind = 0
point_num = []
store_list = []
point_list = []
show_point = []
line_list = []
ball_radius = 1
ball_color = "BLACK"
start_control = False
i = 0

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

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
                    point_num.append(count)
                
                elif(Flag == True and count):
                    pos = f_str.split(' ');
                    pos_ls = list((int(pos[0]), int(pos[1])))
#                     print(pos_ls)
                    store_list.append(pos_ls)
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
                    point_num.append(count)
                
                elif(Flag == True and count):
                    pos = f_str.split(' ');
                    pos_ls = list((int(pos[0]), int(pos[1])))
                    print(pos_ls)
                    store_list.append(pos_ls)
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

def next_file():
    global ind
    global point_list
    global point_begin
    global point_end
    global point_num
    global line_list
    if(point_end < len(store_list) and len(store_list) != 0):
        point_list = []
        line_list = []
        point_end += point_num[ind]
        for i in range(point_begin, point_end):
            point_list.append(store_list[i])
        point_begin += point_num[ind]
        ind += 1
    else:
        pass    
    
# clear the window
def clear_window():
        global point_list
        global line_list
        point_list = []
        line_list = []
        frame.set_canvas_background("White") 
   
# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw
def click(pos):
        point_list.append(list(pos))
        # print(pos)
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
        for point in point_list:
            canvas.draw_circle(point, ball_radius, 2, "Black", ball_color)
        for line in line_list:    
            canvas.draw_line(line[0], line[1], 2, "Olive")
#             frame.set_canvas_background(color_list[i])
#         canvas.draw_line([0,0], [height,width], 2, color_list[i])

# implement step by step
def step_by_step(canvas):
   pass


def list2int(numlist):
    return int(numlist[0])

def del_dup_point():
    global point_list
    del_point_list = []
    [del_point_list.append(i) for i in point_list  if not i in del_point_list]
    point = del_point_list
    return del_point_list

# 修正 將 Fraction 轉型為 str 時會分母為1的情形 
def fix_slope(sr):
    if (len(sr) == 1 or len(sr) == 2):
        return sr + "/1"
    return sr
     
def circumcenter(point_ls):
    # 只有一點
    if(len(point_ls) == 1):
        print("Only one point")
        pass
    # 兩點
    if(len(point_ls) == 2):
        # 兩點平行，垂直線
        if((point_ls[1][1] - point_ls[0][1]) == 0):
            mid = [(point_ls[1][0] + point_ls[0][0]) / 2, (point_ls[1][1] + point_ls[0][1]) / 2]  # 中點
            line_list.append([[mid[0], 0], [mid[0], 600]])
        # 兩點垂直，水平線
        elif((point_ls[1][0] - point_ls[0][0]) == 0):
            mid = [(point_ls[1][0] + point_ls[0][0]) / 2, (point_ls[1][1] + point_ls[0][1]) / 2]  # 中點
            line_list.append([[0, mid[1]], [600, mid[1]]])
        # 任意兩點
        else:    
            slope = str(-1 / Fraction((point_ls[1][0] - point_ls[0][0]), (point_ls[1][1] - point_ls[0][1])))  # 中垂線斜率
            mid = [(point_ls[1][0] + point_ls[0][0]) / 2, (point_ls[1][1] + point_ls[0][1]) / 2]  # 中點
            
            # 畫線兩點
            up = mid
            down = mid
            
            # 修正  
            slope = fix_slope(slope)
            
            # 中垂線方程式
            x_y = slope.split('/')
            x1 = int(x_y[0])
            y1 = int(x_y[1])
            while(up[0] >= 0 and up[1] >= 0 and up[0] <= 600 and up[1] <= 600):
                up = [up[0] - x1 / 2, up[1] - y1 / 2]
            while(down[0] >= 0 and down[1] >= 0 and down[0] <= 600 and down[1] <= 600):
                down = [down[0] + x1 / 2, down[1] + y1 / 2]
#             equ = int(x1) * mid[0] - int(y1) * mid[1]
#             f1 = int(x1) * x + equ
#             f2 = -int(y1) * y + equ
#             cor_x = list2int(solve(f1, x))
#             cor_y = list2int(solve(f2, y))
            print(up, down)
            line_list.append([up, down])
#             print(cor_x, cor_y)
#             print(mid[0], mid[1])
#             print(equ)
        
    if(len(point_ls) == 3):
        # 兩點中垂線斜率
        slope1 = str(-1 / Fraction((point_ls[1][0] - point_ls[0][0]), (point_ls[1][1] - point_ls[0][1])))  
        slope2 = str(-1 / Fraction((point_ls[2][0] - point_ls[1][0]), (point_ls[2][1] - point_ls[1][1])))  
        slope2 = str(-1 / Fraction((point_ls[2][0] - point_ls[0][0]), (point_ls[2][1] - point_ls[0][1])))  
        
        # 兩點中點
        mid1 = [(point_ls[0][0] + point_ls[1][0]) / 2, (point_ls[0][1] + point_ls[1][1]) / 2]
        mid2 = [(point_ls[1][0] + point_ls[2][0]) / 2, (point_ls[1][1] + point_ls[2][1]) / 2]
        
        # 修正  
        slope1 = fix_slope(slope1)
        slope2 = fix_slope(slope2)
        
        #三點共線
        if(slope1 == slope2):
            circumcenter([point_ls[1],point_ls[0]])
            circumcenter([point_ls[2],point_ls[1]])
        else:
            # 中垂線方程式
            m1 = slope1.split('/')
            m2 = slope2.split('/')
            m3 = slope2.split('/')
            x1 = int(m1[0])
            y1 = int(m1[1])
            x2 = int(m2[0])
            y2 = int(m2[1])
            print(point_ls)
            equ1 = int(x1) * mid1[0] - int(y1) * mid1[1]
            equ2 = int(x2) * mid2[0] - int(y2) * mid2[1]
            f1 = int(x1) * x - int(y1) * y - equ1
            f2 = int(x2) * x - int(y2) * y - equ2
            print(slope1, slope2,)
            sol = solve((f1, f2), x, y)
            print(m1 , m2,)
            print(f1 , f2)
            print(round(sol[x], 0), round(sol[y], 0))
        
# Divide and Conquer
def divide_and_conquer():
    pass
# Start the Voronoi Diagram
def run():
    global point_list
    point_list.append([200, 200])
    point_list.append([300, 300])
    point_list.append([400, 400])
    point_list = del_dup_point()
    point_list.sort()
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
btm_fr_c = frame.add_button("Next", next_file, 200);
lable4 = frame.add_label("\n", 1);
btm_fr_wf = frame.add_button("Write File", write_file, 200);
lable3 = frame.add_label("\n", 1);

btm_clear = frame.add_button("Clear window", clear_window, 200);

# start frame
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.start()
