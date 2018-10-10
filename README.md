 $LAN=Python$
 Author : 陳柏憲  Bo-Xian Chen
 Student ID : M053040020
 Date : 2016/10/05

SimpleGUICS2Pygame
>>> https://pypi.python.org/pypi/SimpleGUICS2Pygame

What does the if __name__ == "__main__": do?
>>> http://stackoverflow.com/questions/419163/what-does-if-name-main-do

排序 .sort() , sorted()
>>> http://swaywang.blogspot.tw/2012/05/pythonpythonpython-sorting.html

[程式思路]
觀察之後得知
找出一個三角形所形成的外心，並以外心為基準去做畫線的動作，
最大的問題在於 : 要如何找出
外心彼此相連就可以形成一個Convex hull , 

[數學]
求中點  (x, y) = ((x1 + x2)/2 , (y1 + y2)/2)
兩線垂直 斜率 m1 * m2 = -1
###不求斜率，改求""向量""

向量垂直 (a !=0 and b !=0)
a=(x1, y1)
b=(x2, y2)
a * b = 0  -> x1x2 + y1y2 =0
reference >>> http://mail.smhs.kh.edu.tw/~tch044/formula/colum3.htm

Python - 向量處理
>>>http://ccckmit.wikidot.com/la:vector

演算法筆記 - 利用向量求交點
>>>http://www.csie.ntnu.edu.tw/~u91029/Point.html
證明>>>http://paulbourke.net/geometry/pointlineplane/

Voronoi Diagram
>>>http://students.info.uaic.ro/~emilian.necula/vor2.pdf

Python tk fileDialog 寫檔案
>>>http://stackoverflow.com/questions/19476232/save-file-dialog-in-tkinter

中文的 windows「命令提示字元」(cmd) 編碼預設是：cp950 ，而 Python3 的預設程式碼編碼是：utf-8 (cp65001)
>>>https://read01.com/Rg255.html
>>>http://marsray.pixnet.net/blog/post/61040521-%5Bpython3%5D-%E7%94%A8-python3-%E5%AF%AB%E4%B8%80%E5%80%8B%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2

程式 Bug 
1.特定形式之三點(非常靠近)，有時線會畫錯

![image](https://github.com/abc234466/Voronoi-Diagram/blob/master/voronoi%20diagram.gif)
