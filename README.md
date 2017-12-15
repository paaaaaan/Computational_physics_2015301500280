## 潘祚坚  学号：2015301500280
## 6.6题
# 问题重述
An important feature of a linear equation is that the sum of two solutions is also a solution. One consequence of this is that two wavepacketets will travel independently of each other. An especially clear to demonstrate this is to set up a string with an initial profile such that there are two Gaussian wavepackets, located at different places on the string. These wavepackets (or components of them) may then propagate toward each other and collide. Show that the wavepackets are unaffected by these collisions. That is, show that two such wavepackets pass through each other without changing shape or speed.
# 问题分析
![picture1](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/12.0/analysis.png)
# 数据图像

## 根据上述关系式，可作出两个不同的波在传播过程中相遇造成的相长或相抵，出现一个波包：

![picture2](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/12.0/1.gif)

### 四个不同的波在传播过程中相遇造成的相长或相抵，出现两个波包：
![picture3](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/12.0/2.gif)
# 结论

### 在各波包相遇时振动叠加，而在分离后，各自以原来的形态传播，波包互相不发生影响（波动方程的线性）。

### 源代码（两个图画到心累，感谢上官学姐部分代码）
```python
#第一幅图
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
#第二幅图
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import animation
delta_x=0.01
c=300
delta_t=delta_x/c
r=1
x=np.linspace(0,1,int(1/delta_x)+1)
def next_step(y_previous,y_current):
    y_next=[0]
    c1,c2=2*(1-r**2),r**2
    for i in range(1,len(y_current)-1):
        y_next.append(c1*y_current[i]-y_previous[i]+c2*(y_current[i-1]+y_current[i+1]))
    y_next.append(0)
    return y_next
def after_n_step(y0,y1,n):
    for i in range(n):
        y2=next_step(y0,y1)
        y0,y1=y1,y2
    return y0,y1
k0,x0=1000,0.3
k1,x1=300,0.6
y_initial=[]
for i in range(1+int(1/delta_x)):
    y_initial.append(math.exp(-k0*(i*delta_x-x0)**2)-2*math.exp(-k1*(i*delta_x-x1)**2))
fig = plt.figure() 
ax = plt.axes(xlim=(0, 1), ylim=(-2.01,2.01))
line, = ax.plot([], [], lw=5.)  
plt.title('Waves')
plt.xlabel('x')
plt.ylabel('displacement')
note = ax.text(0.05,1.4,'',fontsize=12)
def init():  
    line.set_data([], []) 
    note.set_text('')
    return line,note
def animate(j):
    y0,y1=after_n_step(y_initial,y_initial,j)
    line.set_data(x, y1)
    return line,note
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=201, interval=50)
plt.show()
```
