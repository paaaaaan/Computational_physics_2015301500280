### 潘祚坚   2015301500280

## 第一题：
###   根据Euler法求出（0s,10s）时间内的每隔0.5秒对应的速度，并作出相应的速度图像。同时根据公式求出其准确的速度与时间关系，与Euler法所得数据对比，数据一致。即：在这种情况下，用Euler法求出某时刻的速度值即为精确值。
   
### 第一题代码
```python
import numpy as np
import pylab as pl
def plot():
    list_time=[0,]
    list_velocity=[0,]
    t=0
    dt=0.5
    v=0
    while t <= 10:
        print("%f,%f" %(t,v))
        t+=dt
        v-=9.8*dt
        list_time.append(t)
        list_velocity.append(v)
    pl.plot(list_time, list_velocity)
    pl.title('plot of v vs. t')
    pl.xlabel('t')
    pl.ylabel('v')
    pl.xlim(0.0,10.0)
    pl.ylim(-100.0,0.0)
    pl.show()
plot()
```

### 第三题：
### 根据Euler法求出（0s,20s）时间内的每隔0.1秒对应的速度，并作出相应的速度图像，由图像可知当时间t趋近10s时，速度v无限接近于10m/s,并当t=10s时，速度v=10m/s。当t>10s时，速度v保持10m/s不变，即为恒定值。
### 其物理意义即为当速度v=10m/s时，由加速度a=0，此后速度不发生变化，即始终保持为10m/s。

### 第三题代码
```python
import numpy as np
import pylab as pl
def plot():
    list_time=[0,]
    list_velocity=[0,]
    t=0
    dt=0.1
    v=0
    while t <= 20:
        print("%f,%f" %(t,v))
        t+=dt
        v=v+(10-v)*dt
        list_time.append(t)
        list_velocity.append(v)
    pl.plot(list_time, list_velocity)
    pl.title('plot of v vs. t')
    pl.xlabel('t')
    pl.ylabel('v')
    pl.xlim(0.0,20.0)
    pl.ylim(0.0,10.0)
    pl.show()
plot()
```
