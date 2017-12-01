#### 潘祚坚 2015301500280

# 炮打翼龙

## 游戏说明
### 游戏思路借鉴：[4399炮轰外星小怪](http://www.4399.com/flash/192577_2.htm)  额，这个要好玩多了，根本停不下来，已玩通关
### 操作：可以通过w、a、s、d键控制大炮的位置，用鼠标调整射击角度，点击鼠标左键发射炮弹。翼龙从右侧边界随机位置飞出，发射炮弹即可击中翼龙。
## 游戏效果
## 戳下面这个链接，点击"download"或者"view raw"可下载试玩视频，视频有游戏音效，视频不大，只有6.5M
## 戳这里↓↓↓
## [试玩视频](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/files/2017.12.01-16.50.25.mp4)
### 下面是试玩视频前三十秒转换的gif
![游戏录屏](https://github.com/paaaaaan/Computational_physics_2015301500280/blob/files/gif.gif)
### BUG:在炮弹击中翼龙的时候设置了一张爆炸的图片，但是有时候击中了没出现爆炸图
### 本次做这个小游戏的一些感想：
### （1）以前觉得做游戏时间很高端的事，但自己尝试过后感觉也并不是很难，有信心了，虽然自己做的很low
### （2）自己编程能力不太够，出了好多次 BUG 但老是搞不清楚问题出在哪，有时候就是很简单的问题没看出来
## 游戏代码
```python
import pygame
from pygame.locals import *
import math
import random
pygame.init()
width, height = 1000, 1000
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
cannonpos=[100,800]
acc=[0,0]
shells=[]
badtimer=100
badtimer1=0
dragons=[[640,100]]
pygame.mixer.init()
cannon = pygame.image.load(r"H:\1.png")#大炮图片
shell = pygame.image.load(r"H:\2.png")#炮弹图片
background = pygame.image.load(r"H:\5.png")#背景图片
dragonimg1 = pygame.image.load(r"H:\3.png")#翼龙图片
bomb = pygame.image.load(r"H:\6.png")
dragonimg=dragonimg1#重复翼龙图片
enemy = pygame.mixer.Sound(r"H:\2.wav")#击中音效
shoot = pygame.mixer.Sound(r"H:\1.wav")#炮弹发射声音
enemy.set_volume(0.05)#设置音量大小
shoot.set_volume(0.05)
while 1:
    badtimer-=1
    screen.fill(0)
    screen.blit(background,(0,0))#显示背景图片
    position = pygame.mouse.get_pos()#鼠标位置读取
    angle = math.atan2(position[1]-(cannonpos[1]+32),position[0]-(cannonpos[0]+26))#根据鼠标位置确定大炮的角度
    cannonrot = pygame.transform.rotate(cannon, 360-angle*57.29)
    cannonpos1 = (cannonpos[0]-cannonrot.get_rect().width/2, cannonpos[1]-cannonrot.get_rect().height/2)
    screen.blit(cannonrot, cannonpos1)#显示大炮的位置
    for bullet in shells:
        index=0
        velx=math.cos(bullet[0])*20#定义炮弹的横向速度大小，此处直接设为直线运动
        vely=math.sin(bullet[0])*20#定义炮弹的纵向速度大小
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-100 or bullet[1]>1000 or bullet[2]<-100 or bullet[2]>1000:
            shells.pop(index)
        index+=1
        for projectile in shells:
            arrow1 = pygame.transform.rotate(shell, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    if badtimer==0:
        dragons.append([1000, random.randint(0,1000)])#定义翼龙出现的位置（随机分布在右侧边缘）
        badtimer=200-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=8
    index=0
    for dragon in dragons:#定义翼龙移动速度的大小
        if dragon[0]<-64:
            dragons.pop(index)
        dragon[0]-=5
        index+=1
    for dragon in dragons:
        screen.blit(dragonimg, dragon)#显示翼龙
    badrect=pygame.Rect(dragonimg.get_rect())#设置龙所在的矩形区域
    badrect.top=dragon[1]#龙的顶部位置
    badrect.left=dragon[0]#龙的左侧位置
    index1=0
    for bullet in shells:
        bullrect=pygame.Rect(shell.get_rect())#设置炮弹的矩形区域
        bullrect.left=bullet[1]#炮弹的左侧位置
        bullrect.top=bullet[2]#炮弹的顶部位置
        if badrect.colliderect(bullrect):#如果炮弹击中了翼龙，即两者的矩形区域有交叉
            screen.blit(bomb,(badrect.left,badrect.top))#显示爆炸的图片
            enemy.play()#出现爆炸的音效
            dragons.pop(index1)#翼龙消失
            shells.pop(index1)#炮弹消失
        index1+=1
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)
        if event.type == pygame.KEYDOWN:#按键wasd的设置
           if event.key==K_w:
               keys[0]=True
           elif event.key==K_a:
               keys[1]=True
           elif event.key==K_s:
               keys[2]=True
           elif event.key==K_d:
               keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                   keys[2]=False
            elif event.key==pygame.K_d:
                   keys[3]=False
        if event.type==pygame.MOUSEBUTTONDOWN:#点击鼠标发射炮弹
            shoot.play()
            position=pygame.mouse.get_pos()#鼠标位置读取
            acc[1]+=1
            shells.append([math.atan2(position[1]-(cannonpos1[1]+32),position[0]-(cannonpos1[0]+26)),cannonpos1[0]+32,cannonpos1[1]+32])
    if keys[0]:
        cannonpos[1]-=5#前后左右移动大炮
    elif keys[2]:
        cannonpos[1]+=5
    if keys[1]:
        cannonpos[0]-=5
    elif keys[3]:
        cannonpos[0]+=5
    
```

