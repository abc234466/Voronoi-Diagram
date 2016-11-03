#------------------------------------------
# $LAN=Python$
# Author : 陳柏憲  Bo-Xian Chen
# Student ID : M053040020
# Date : 2016/10/05
#------------------------------------------

#[            Voronoi Diagram             ]

SimpleGUICS2Pygame
>>> https://pypi.python.org/pypi/SimpleGUICS2Pygame

What does the if __name__ == "__main__": do?
>>> http://stackoverflow.com/questions/419163/what-does-if-name-main-do


[程式思路]
觀察之後得知
找出一個三角形所形成的外心，並以外心為基準去做畫線的動作，
最大的問題在於 : 要如何找出
外心彼此相連就可以形成一個Convex hull , 

[數學]
求終點  (x, y) = ((x1 + x2)/2 , (y1 + y2)/2)