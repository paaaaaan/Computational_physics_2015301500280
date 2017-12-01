#### 潘祚坚 2015301500280
# 题目4.12
## 题目
### Investigate the effect of Jupiter on Mars(考虑木星对火星轨道的影响)
## 分析
## 数据图像
# 题目4.14的尝试
## 题目
### 通过编写程序模拟出太阳、地球、月亮三体的运动，并注意两点：1、月球绕地球和地球绕太阳时间尺度不同  2、设定月球初速度时需考虑地球的速度
## 代码
```python
import numpy as np
import matplotlib.pyplot as plt
import math
list_xearth=[1.496*(math.pow(10,8)),]
list_yearth=[0,]
list_xmoon=[(1.496*(math.pow(10,8))+384000),]
list_ymoon=[0,]
list_rearth=[1.496*(math.pow(10,8)),]
list_rmoon=[(1.496*(math.pow(10,8))+384000),]
#list_vxearth=[0,]#以秒为速度单位
#list_vyearth=[29.78,]
#list_vxmoon=[0,]
#list_vymoon=[30.803,]
list_vxearth=[0,]
list_vyearth=[940000000,]
list_vxmoon=[0,]
list_vymoon=[(940000000+32261328),]
dt=0.01#年为单位
vyearth=940000000#公里每年
vxearth=0
vymoon=(940000000+32261328)#公里每年
vxmoon=0
#vyearth=29.78#公里每秒
#vxearth=0
#vymoon=(29.78+1.023)#公里每秒
#vxmoon=0
xearth=1.496*(math.pow(10,8))#单位公里
yearth=0
xmoon=(1.496*(math.pow(10,8))+384000)#单位公里
ymoon=0
mmoon=7.349*(math.pow(10,22))
mearth=5.965*(math.pow(10,24))
msun=1.9891*(math.pow(10,30))
t=0
while(t<1):
    rearth=math.sqrt(xearth*xearth+yearth*yearth)
    rmoon=math.sqrt(xmoon*xmoon+ymoon*ymoon)
    rem=math.sqrt((xearth-xmoon)*(xearth-xmoon)+(yearth-ymoon)*(yearth-ymoon))
    vxearth=vxearth-4*(math.pi)*(math.pi)*xearth*dt/(rearth*rearth*rearth)-4*(math.pi)*(math.pi)*mmoon*(xearth-xmoon)*dt/msun/(rem*rem*rem)
    vyearth=vyearth-4*(math.pi)*(math.pi)*yearth*dt/(rearth*rearth*rearth)-4*(math.pi)*(math.pi)*mmoon*(yearth-ymoon)*dt/msun/(rem*rem*rem)
    vxmoon=vxmoon-4*(math.pi)*(math.pi)*xmoon*dt/(rmoon*rmoon*rmoon)-4*(math.pi)*(math.pi)*mearth*(xearth-xmoon)*dt/msun/(rem*rem*rem)
    vymoon=vymoon-4*(math.pi)*(math.pi)*ymoon*dt/(rmoon*rmoon*rmoon)-4*(math.pi)*(math.pi)*mearth*(yearth-ymoon)*dt/msun/(rem*rem*rem)
    xearth=xearth+vxearth*dt
    yearth=yearth+vyearth*dt
    xmoon=xmoon+vxmoon*dt
    ymoon=ymoon+vymoon*dt
    t=t+dt
    list_xearth.append(xearth)
    list_yearth.append(yearth)
    list_xmoon.append(xmoon)
    list_ymoon.append(ymoon)
    list_vxearth.append(vxearth)
    list_vyearth.append(vyearth)
    list_vxmoon.append(vxmoon)
    list_vymoon.append(vymoon)
    list_rearth.append(rearth)
    list_rmoon.append(rmoon)
    print(xearth,yearth,xmoon,ymoon,vxearth,vyearth,vxmoon,vymoon,rem)
plt.plot(list_xearth, list_yearth,'.',label='x,y')
plt.title('plot of y vs. x')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-200000000,200000000)
plt.ylim(-200000000,200000000)
plt.show()
```
### 运行程序后得不到正确的结果，只好换题4.12
