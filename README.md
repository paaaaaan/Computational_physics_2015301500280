## 2.9题

# 问题重述
  
  **同时考虑空气阻力和不同高度下空气密度的影响，计算炮弹的轨迹。调整不同的角度并计算射程最大的角度值。**

# 问题分析

![fenxi](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/4.0/exercise04.png)
 
# 数据图像

![figure](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/4.0/Figure_1.png)

## 源代码
import numpy as np
import pylab as pl
import math
def plot():
    list_xcoo=[0,]
    list_ycoo=[0,]
    t=0
    B=0.04
    dt=1
    v=0.7
    vx=0.7*(math.cos(math.radians(50)))
    vy=0.7*(math.sin(math.radians(50)))
    x=0
    y=0
    angel=50
    while y>=0:
        print("%f,%f,%f,%f,%f,%f" %(x,y,vx,vy,angel,t))
        t+=dt
        B=(math.exp(-y*0.1))*B
        angel=(math.atan(vy/vx))*180/(math.pi)
        vx=v*(math.cos(math.radians(angel)))
        vy=v*(math.sin(math.radians(angel)))
        v=math.sqrt(vx*vx+vy*vy)
        x+=vx*dt
        y+=vy*dt
        vx-=B*v*vx*dt
        vy=vy-0.0098*dt-B*v*vy*dt
        list_xcoo.append(x)
        list_ycoo.append(y)
    pl.plot(list_xcoo, list_ycoo)
    pl.title('plot of y vs. x')
    pl.xlabel('x')
    pl.ylabel('y')
    pl.xlim(0.0,200.0)
    pl.ylim(0.0,50.0)
    pl.show()
plot()
