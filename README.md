## 潘祚坚  学号：2015301500280
## 6.6题
# 问题重述
An important feature of a linear equation is that the sum of two solutions is also a solution. One consequence of this is that two wavepacketets will travel independently of each other. An especially clear to demonstrate this is to set up a string with an initial profile such that there are two Gaussian wavepackets, located at different places on the string. These wavepackets (or components of them) may then propagate toward each other and collide. Show that the wavepackets are unaffected by these collisions. That is, show that two such wavepackets pass through each other without changing shape or speed.
# 问题分析
![picture1](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/12.0/analysis.png)
# 数据图像

## 根据上述关系式，可作出两个不同的波在传播过程中相遇造成的相长或相抵：

![picture2](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/12.0/1.gif)


![picture3](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/12.0/2.gif)
# 结论

## 在各波包相遇时振动叠加，而在分离后，各自以原来的形态传播，波包互相不发生影响（波动方程的线性）。

### 源代码
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
c=1
l=1
dt=0.01
dx=0.01
x0=0.3
x1=l-x0
r=c*dt/dx
k=1000
t=300
N=(int(t/dt))
n=(int(l/dx))+1
class wave(object):
    """docstring for wave"""
    def __init__(self):
        self.x=np.linspace(0,1,n)
        self.y0=np.exp(-k*(self.x-x0)**2)
        self.y=[self.y0]
        self.temp_y=np.linspace(0,0,n)
        for j in range(n-2):
            self.temp_y[j+1]=2*(1-r**2)*self.y0[j+1]-self.y0[j+1]+r**2*(self.y0[j+2]+self.y0[j])
        self.y.append(self.temp_y)
        #print self.y0
    def update(self):
        self.new_y=np.linspace(0,0,n)
        for j in range(n-2):
            self.new_y[j+1]=2*(1-r**2)*self.y[-1][j+1]-self.y[-2][j+1]+r**2*(self.y[-1][j+2]+self.y[-1][j])
    def fire(self):
        while (len(self.y)<=(N+1)):
            self.update()
            self.y.append(self.new_y)
Har=wave()
Har.fire()
print (Har.y[1])
fig = plt.figure(figsize=(6,6))
ax = plt.axes(xlim=(0, l), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=2)
def init():  
    line.set_data([], [])  
    return line,
def animate(i):
    x = Har.x
    y = Har.y[i]
    line.set_data(list(x), list(y))   
    return line,
anim=animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=25)
plt.title('wave')
plt.show()
```
