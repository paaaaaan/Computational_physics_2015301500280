### 潘祚坚 2015301500280

## 题目2.20
### 计算旋转对快球的作用，求出1000转每分钟的角速度如何影响轨迹。

## 问题分析
![picture](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/5.0/picture4.png)

## 数据结果
### 当角速度为1000rpm时，y、z随x变化曲线；
![picture](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/files/picture5.png)
### 当角速度为1500rpm时，y、z随x变化曲线；
![picture](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/files/picture6.png)
### 当角速度为2000rpm时，y、z随x变化曲线；
![picture](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/files/picture7.png)
## 结论
### 由三组不同角速度情况下，y、z随x变化图像可知，当角速度越来越大时，z的变化越来越明显。即上下两部分的向心力之差越来越大，导致z变化加快，与实际相符合。
 
## 源代码
```python
import numpy as np
import matplotlib.pyplot as plt
import math
plt.figure()
list_xcoo=[0,]
list_ycoo=[0,]
list_zcoo=[0,]
B=0.00004
dt=0.01
v=31.2928
x=0
y=3.5
z=0
vx=v
vy=0
vz=0
w=200
while x<50: 
    B=(math.exp(-y*0.1))*B       
    x+=vx*dt
    y+=vy*dt
    z+=vz*dt
    vx=vx-B*v*vx*dt
    vy=vy-9.8*dt
    vz=vz+0.00041*vx*w*dt
    v=math.sqrt(vx*vx+vy*vy+vz*vz)
    print("%f,%f,%f,%f,%f,%f" %(x,y,z,vx,vy,vz))  
    list_xcoo.append(x)
    list_ycoo.append(y)
    list_zcoo.append(z)
plt.plot(list_xcoo, list_ycoo)
plt.plot(list_xcoo, list_zcoo)
plt.title('plot of y/z vs. x')
plt.xlabel('x(m)')
plt.ylabel('y or z(m)')
plt.xlim(0.0,60)
plt.ylim(-4.0,4.0)
plt.show()
```

