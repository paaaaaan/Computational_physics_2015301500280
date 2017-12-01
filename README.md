#### 潘祚坚 2015301500280
# 题目3.31
Study teh behavior for other types of tables.One interesting possibility is a square table with a circular interier wall located either in the center.Another possibility is an elliptical table.
## 问题分析
![exercise09](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/8.0/exercise09.png)
## 数据图像
### 当桌面为正方形时，设定小球初速度使小球在桌面上碰撞，得到其运动轨迹如下图：
![picture1](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/8.0/1.png)
### 其对应的水平方向速度与水平坐标的关系如下图，即水平速度只取正负两个值：
![picture2](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/8.0/2.png)
### 当桌面的形状为椭圆形时，根据分析中速度变化公式编程可运行得到以下图像，此时设定的α=0.001：
![picture3](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/8.0/3.png)
### 当α值出现较小变化时，会引起图像的较大改变。
## 结论
### 由上述图像可知，当桌面形状为椭圆时，参数改变小量，但是得到的图像会出现较大的变化，出现了混沌现象
## 源代码
### （在处理球与不规则桌面的碰撞时，自己写的代码老是跑不出来正确图像，这里借鉴了王森同学的代码，非常感谢）
- [code](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/8.0/code)
