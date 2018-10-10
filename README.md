# **Voronoi Diagram**
**Author : 陳柏憲 BoXian Chen**\
**Goal : Voronoi Diagram within four points**
---
**Package :**

* SimpleGUICS2Pygame
    >https://pypi.python.org/pypi/SimpleGUICS2Pygame

---
**程式思路**
1. 觀察之後得知 找出一個三角形所形成的外心，並以外心為基準去做畫線的動作， 最大的問題在於 : 要如何找出 外心彼此相連就可以形成一個Convex hull。
2. 求中點 (x, y) = ((x1 + x2)/2 , (y1 + y2)/2) 兩線垂直 斜率 m1 * m2 = -1 不求斜率，改求**向量**
3. 向量垂直 (a !=0 and b !=0) a=(x1, y1) b=(x2, y2) a * b = 0 -> x1x2 + y1y2 =0
    >http://mail.smhs.kh.edu.tw/~tch044/formula/colum3.htm
4. 演算法筆記 - 利用向量求交點
    >http://www.csie.ntnu.edu.tw/~u91029/Point.html<br>
    >Prove : http://paulbourke.net/geometry/pointlineplane/
7. Voronoi Diagram
    >http://students.info.uaic.ro/~emilian.necula/vor2.pdf

---
**疑難雜症**
1. 中文的 windows「命令提示字元」(cmd) 編碼預設是：cp950 ，而 Python3 的預設程式碼編碼是：utf-8 (cp65001)
    >https://read01.com/Rg255.html#.W74ylmgzZPY<br>
    >http://marsray.pixnet.net/blog/post/61040521-%5Bpython3%5D-%E7%94%A8-python3-%E5%AF%AB%E4%B8%80%E5%80%8B%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2

---
**BUG**
* 特定形式之三點(非常靠近)，有時線會畫錯

---
**範例圖片**
![image](https://github.com/abc234466/Voronoi-Diagram/blob/master/voronoi%20diagram.gif)
